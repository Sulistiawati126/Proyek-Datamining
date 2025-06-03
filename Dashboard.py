import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard", layout="wide")

# Judul
st.title("📊 Dashboard Analisis Ulasan Pengguna Shopee")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Data ulasan Shopee tentang COD.csv")
    return df

df = load_data()

# Tampilkan data mentah
if st.checkbox("Tampilkan data mentah"):
    st.write(df.head())

# Informasi dasar
st.subheader("Informasi Umum Dataset")
st.write("Jumlah Ulasan:", df.shape[0])
st.write("Kolom:", list(df.columns))

# Visualisasi rating
st.subheader("Distribusi Rating")
fig, ax = plt.subplots()
sns.countplot(data=df, x="Rating", ax=ax, palette="viridis")
st.pyplot(fig)

# Wordcloud (jika ingin analisis teks lebih lanjut)
st.subheader("Contoh Ulasan")
st.write(df["Ulasan"].dropna().sample(5))

# Filter ulasan berdasarkan rating
st.subheader("Filter Ulasan Berdasarkan Rating")
rating_filter = st.selectbox("Pilih Rating", sorted(df["Rating"].unique()))
filtered = df[df["Rating"] == rating_filter]
st.write(filtered[["Ulasan"]].dropna().sample(min(10, len(filtered))))


