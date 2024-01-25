#######################
# Import libraries
# import altair as alt
import pandas as pd
import streamlit as st


#######################
# Page configuration
st.set_page_config(
    page_title="dakarvente",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# alt.themes.enable("dark")


df = pd.read_csv("data_scraped_with_beautifulsoup_on_dakarvente/dakarvente.csv")


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
    pass

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

elif page == pages[3]:
    st.write("### Analyse de données")

    # st.dataframe(data)
