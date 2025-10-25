import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initial configuration
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

# -------------------------------
# Load data
# -------------------------------
st.title("CORD-19 Data Explorer")
st.write("A simple exploration of COVID-19 research articles")

# Upload or local file loading
uploaded = st.sidebar.file_uploader("Upload CSV file (metadata_prepared.csv)", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
else:
    try:
        df = pd.read_csv("metadata_prepared.csv")
    except:
        st.warning("Please upload the CSV file to get started.")
        st.stop()

# -------------------------------
# Data preparation
# -------------------------------
if "publish_time" in df.columns:
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year

df["journal"] = df["journal"].fillna("Unknown")

# -------------------------------
# Interactive filters
# -------------------------------
years = sorted(df["year"].dropna().unique())
if years:
    year_range = st.sidebar.slider("Select year range", int(min(years)), int(max(years)), (int(min(years)), int(max(years))))
    df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]
else:
    df_filtered = df

# -------------------------------
# Visualizations
# -------------------------------
st.header("📊 Visualizations")

# Chart 1 — Publications by year
st.subheader("Number of publications over the years")
year_counts = df_filtered["year"].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values)
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of publications")
ax1.set_title("Publications over the years")
st.pyplot(fig1)

# Chart 2 — Top 10 Journals
st.subheader("Top 10 Journals")
top_journals = df_filtered.groupby('journal')['cord_uid'].count().sort_values(ascending=False).head(10)
fig2, ax2 = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax2)
ax2.set_xlabel("Number of articles")
ax2.set_ylabel("Journal")
ax2.set_title("Top 10 Journals with the Most Publications")
st.pyplot(fig2)

# Chart 3 — Most frequent words in titles
st.subheader("Top 10 Most Frequent Words in Titles")
word_counts = df_filtered['title'].str.split().explode().value_counts().head(10)
fig3, ax3 = plt.subplots()
ax3.bar(word_counts.index, word_counts.values)
ax3.set_xlabel("Word")
ax3.set_ylabel("Frequency")
ax3.set_title("Most Frequent Words in Titles")
st.pyplot(fig3)

# Chart 4 — Publications by source
st.subheader("Distribution of Publications by Source")
source_counts = df_filtered["source_x"].value_counts().sort_index()
fig4, ax4 = plt.subplots()
ax4.bar(source_counts.index, source_counts.values)
ax4.set_xlabel("Source")
ax4.set_ylabel("Number of articles")
ax4.set_title("Distribution of Publications by Source")
st.pyplot(fig4)

# -------------------------------
# Data sample
# -------------------------------
st.header("📄 Data Sample")
st.dataframe(df_filtered.head(50))

# -------------------------------
# Conclusion / Reflection
# -------------------------------
st.markdown("---")
st.write("""
🧠 Reflection\n
During this project, I was able to understand the complete data analysis workflow in practice — from data preparation to the communication of insights.\n
I learned how to:\n
    1. Identify and handle missing data;\n
    2. Convert data types and create derived columns;\n
    3. Generate visualizations that summarize complex information in an accessible way;\n
\n
Finally, I used Streamlit to share my analyses in a visual and interactive manner.\n
The main challenge was cleaning the data, as the original file contained many missing values and inconsistent formats.\n
This experience reinforced the importance of understanding and preparing data properly before performing any analysis.
""")
