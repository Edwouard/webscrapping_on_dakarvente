#######################
# Import libraries
# import altair as alt
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

#######################
# Page configuration
st.set_page_config(
    page_title="dakarvente",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# alt.themes.enable("dark")


df = pd.read_csv(
    "data_scraped_with_beautifulsoup_on_dakarvente/dakarvente_reshaped.csv"
)


categories = df["category"].unique()

# st.sidebar.title("Sommaire")

# pages = [
#     "Présentation du projet",
#     "Exploration des données",
#     "Analyse de données",
# ]

# page = st.sidebar.radio("Aller vers la page :", pages)


with st.sidebar:
    st.sidebar.title("Sommaire")

    pages = [
        "Présentation du projet",
        "Données scrappées",
        "Exploration des données",
        "Analyse de données",
    ]

    page = st.sidebar.radio("Aller vers la page :", pages)


if page == pages[0]:
    st.title("Présentation du projet")
    st.write("Le projet consistait à :")
    st.write(
        "1. Scraper et nettoyer les données sur toutes les pages des urls ci-dessous en utilisant BeautifulSoup"
    )
    st.write(
        """
- url 1 : https://dakarvente.com/annonces-rubrique-vehicules-2.html
- url 2 : https://dakarvente.com/annonces-categorie-motos-3.html
- url 3 https://dakarvente.com/annonces-categorie-location-de-vehicules-8.html
- url 4 : https://dakarvente.com/annonces-categorie-telephones-32.html
- url 5 : https://dakarvente.com/annonces-categorie-appartements-louer-10.html
- url 6 : https://dakarvente.com/annonces-categorie-appartements-vendre-61.html
- url 7 : https://dakarvente.com/annonces-categorie-terrains-vendre-13.htmll

NB: Pour chaque URL, il s'agissait de scrapper les variable
-V1: details
-V2 : prix
-V3 : adresse
-V4: image_lien
"""
    )

    st.write(
        "2. Scraper sans nettoyer les données sur 50 pages en utilisant Web Scraper"
    )
    st.write(
        """
- url 1 : https://dakarvente.com/annonces-rubrique-vehicules-2.html
V1: marque, V2 : prix, V3 : adresse, V4: image_lien
- url 2 : https://dakarvente.com/annonces-categorie-motos-3.html
V1: marque, V2 : prix, V3 : adresse, V4: image_lien
- url 3 https://dakarvente.com/annonces-categorie-location-de-vehicules-8.html
V1: marque, V2 : prix, V3 : adresse, V4: image_lien
- url 4 : https://dakarvente.com/annonces-categorie-telephones-32.html
V1: marque, V2 : prix, V3 : adresse, V4: image_lien
"""
    )
    st.write(
        "3. Mettre en place une app déployée en utilisant streamlit, sur laquelle on peut télécharger les données scraper à travers BeautifulSoup et Web Scraper"
    )

elif page == pages[1]:
    st.write("### Data scraped with web scraper")

    data_scrapped = {
        "vehicles": "dakarvente_vehicules.csv",
        "motos": "dakarvente_motos.csv",
        "Phones": "dakarvente_telephones.csv",
    }

    selected_data = st.selectbox("Select data ", data_scrapped)
    data_path = (
        "./data_scraped_with_web_scraper_on_dakarvente/" + data_scrapped[selected_data]
    )

    st.write(pd.read_csv(data_path))

    st.write("### Data scraped with BeautifulSoup")
    st.dataframe(df)

elif page == pages[2]:
    st.write("### Exploration des données")

    # selected_category = st.selectbox("Filtrer par catégorie", categories)
    categories = st.multiselect("Pick the category", df["category"].unique())
    addresses = st.multiselect("Pick the adress", df["adress"].unique())
    # data = df[df["category"] == selected_category]
    st.dataframe(df[df["category"].isin(categories) & df["adress"].isin(addresses)])

    st.write("Dimensions du dataframe :")

    st.write(df.shape)

    if st.checkbox("Afficher les valeurs manquantes"):
        st.dataframe(df.isna().sum())

    if st.checkbox("Afficher les doublons"):
        st.write(df.duplicated().sum())

    with st.expander("Statistiques descriptives"):
        st.write(df.describe())

elif page == pages[3]:
    st.write("### Analyse de données")
    col1, col2 = st.columns((2))
    fig = px.scatter(df, x="price", y="adress", color="category")
    st.plotly_chart(fig, use_container_width=True, height=200)

    # with col1:
    #     categories = st.multiselect("Pick the category", df["category"].unique())
    #     df1 = df[df["category"].isin(categories)]

    # with col2:
    #     fig = px.scatter(df1, x="price", y="adress", color="category")
    #     fig.show()

    # with st.expander("Afficher les histogrammes"):
    #     st.subheader("Histogrammes:")
    #     for col in df.columns:
    #         fig, ax = plt.subplots()
    #         plt.hist(df[col], bins=10, edgecolor="k", color="purple")
    #         plt.xlabel("Valeurs")
    #         plt.ylabel("Fréquence")
    #         plt.title(f"Histogramme de {col}")
    #         st.pyplot(fig)

    # with st.expander("Afficher la matrice de corrélation"):
    #     st.subheader("Matrice de corrélation:")
    #     corr_matrix = df.corr()
    #     sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    #     plt.title("Matrice de corrélation")
    #     st.pyplot()
# st.dataframe(data)
