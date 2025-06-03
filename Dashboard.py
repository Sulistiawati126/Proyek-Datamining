import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Ulasan Shopee", layout="wide")

# --- Load data ---
@st.cache_data
def load_data():
    df = pd.read_csv("Data ulasan Shopee tentang COD.csv")
    df.head(1160)
    return df

df = load_data()

# --- Tampilkan judul dan data mentah ---
st.title("📊 Dashboard Analisis Ulasan Shopee")
st.subheader("Data Mentah")
st.dataframe(df)

# --- Cek nama kolom ---
st.subheader("Nama Kolom di Dataset")
st.write(df.columns)

# --- Visualisasi rating (ganti nama kolom sesuai dataset kamu) ---
if "Rating" in df.columns:
    st.subheader("Distribusi Rating")

    fig, ax = plt.subplots()
    sns.countplot(data=df, x="Rating", ax=ax, palette="viridis")
    st.pyplot(fig)
else:
    st.warning("Kolom 'Rating' tidak ditemukan. Coba cek nama kolom yang benar.")
