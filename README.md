# Streamlit ORD Downloader
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ord-downloader.streamlit.app/)

The **Open Reaction Database (ORD)** is an open-source database for chemical synthesis reactions, collecting a variety of conditions and records required for different chemical syntheses, which can be used for machine learning or deep learning. ORD provides a user-friendly online interactive interface (https://open-reaction-database.org/client/browse). However, for beginners, what they need is a simple *download button* to get the data in `.csv` format, which is not obviously available on this page. 

In addition to the issue of download convenience, another problem is as follows: using ORD requires the installation of `ord-schema` initially. However, if you do not have administrative permissions to install `PostgreSQL` and `libpq-dev` (see https://stackoverflow.com/questions/11618898/pg-config-executable-not-found), `ord-schema` will essentially plunge into an "environment hell", making it impossible to install and use. Therefore, this project also saves you from the trouble of setting up the environment.

The `Granda_Perera_ml_example.ipynb` in ORD's Github page provides the corresponding operation for the above requirement. This project extracts the corresponding code from this `Granda_Perera_ml_example.ipynb`, allowing users to easily download the required ORD data through the powerful UI interactive interface of *Streamlit*🎈.
# LICENSE
MIT