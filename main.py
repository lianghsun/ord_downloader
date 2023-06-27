import ord_schema
from ord_schema import message_helpers, validations
from ord_schema.proto import dataset_pb2
import pandas as pd
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw, PandasTools
import re
import os
import base64
import wget

st.set_page_config(page_title='ORD Downloader', page_icon='🧑‍🔬')

# Main app
def main():
    st.title("🧑‍🔬 ORD Downloader")
    
    with st.expander('🤔 __What\'s this for?__'):
        st.markdown("The **Open Reaction Database (ORD)** is an open-source database for chemical synthesis reactions, collecting a variety of conditions and records required for different chemical syntheses, which can be used for machine learning or deep learning. ORD provides a user-friendly online interactive interface (https://open-reaction-database.org/client/browse). However, for beginners, what they need is a simple *download button* to get the data in `.csv` format, which is not obviously available on this page. The `Granda_Perera_ml_example.ipynb` in ORD's Github page provides the corresponding operation for the above requirement. This project extracts the corresponding code from this `Granda_Perera_ml_example.ipynb`, allowing users to easily download the required ORD data through the powerful UI interactive interface of *Streamlit*🎈.")
        
    dataset_id = st.text_input(
        label='🪪 The **Dataset ID** of ORD pages: https://open-reaction-database.org/client/browse',
        key='dataset_id',
        help='Please refer to https://open-reaction-database.org/client/browse',
        placeholder='ord_dataset-00005539a1e04c809a9a78647bea649c',
        
    )
    
    if dataset_id:
        match = re.search('ord_dataset-(\w{2})', dataset_id)
        if match:
            url = f"https://github.com/open-reaction-database/ord-data/blob/main/data/{match.group(1)}/{dataset_id}.pb.gz?raw=true"
            output_filename = f"{dataset_id}.pb.gz"
            
            if os.path.exists(output_filename):
                os.remove(output_filename)
            
            try:
                pb = wget.download(url, out=output_filename)
                data = message_helpers.load_message(pb, dataset_pb2.Dataset)
                valid_output = validations.validate_message(data)
                
                if 'result' not in st.session_state:
                    st.session_state.result = ''
                
                st.session_state.result = message_helpers.messages_to_dataframe(data.reactions, drop_constant_columns=True)
                
            except:
                download_error_handler()
            
        else:
            download_error_handler()
            
    if 'result' in st.session_state:
        st.header('Result')
        st.write(st.session_state.result)
        
        st.header('Download')
        columns = list(st.session_state.result.columns)
        st.multiselect(
            label='(Optional) Please select the cols you need. The default selection includes all columns.',
            options=columns,
            default=columns,
            key='selected_cols',
            help='Create new dataframe containing only columns to be used.',
        )
        # st.markdown(get_table_download_link(st.session_state.result[st.session_state.selected_cols]), unsafe_allow_html=True)
        
        b64 = st.session_state.result[st.session_state.selected_cols].to_csv(index=False).encode('utf-8')
        st.download_button(
            label='Download data as CSV',
            data=b64,
            file_name=f"{st.session_state.dataset_id}.csv",
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
