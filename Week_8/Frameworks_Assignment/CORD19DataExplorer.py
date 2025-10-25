import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
# import seaborn as sns  # Optional library for enhanced visualizations

# Load the dataset into a DataFrame
# Load only the first 5000 rows and selected columns to save memory
cols = ['cord_uid', 'title', 'abstract', 'publish_time', 'journal', 'authors', 'source_x']
df = pd.read_csv('metadata.csv', usecols=cols, nrows=5000, dtype=str, low_memory=False)

# Preview the first 5 rows to inspect the structure and columns
df_preview = pd.read_csv('metadata.csv', nrows=5)
print(df_preview.head())

# Display basic structure information
print("Dimensions:\n[rows | columns]")
print(df.shape)
print("\nData types:")
print(df.dtypes)

# Check for missing (null) values
print("\n===== Missing values by column =====")
print(df.isnull().sum())

######### MISSING DATA HANDLING #########
# Fill missing values in key columns
df['title'] = df['title'].fillna('No title')
df['abstract'] = df['abstract'].fillna('No abstract')
df['journal'] = df['journal'].fillna('Unknown')
df['authors'] = df['authors'].fillna('Unknown')

# Remove duplicate rows based on title and publication date
df = df.drop_duplicates(subset=['title', 'publish_time'])

# Save a cleaned version of the dataset
df.to_csv('metadata_prepared.csv', index=False)
print("File saved: metadata_prepared.csv")

# Load the cleaned/prepared dataset
df = pd.read_csv('metadata_prepared.csv')

# Convert the publish_time column to datetime format (handling empty strings)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract publication year for time-based analysis
df['year'] = df['publish_time'].dt.year
print("Publication years:")
print(df['year'].head())

# Add a column with abstract word counts
df['word_count'] = df['abstract'].str.split().str.len()

############## BASIC DATA ANALYSIS AND VISUALIZATIONS ##############

# Count articles by publication year
df.groupby('year')['cord_uid'].count().plot(kind='bar', figsize=(10, 6))
plt.xlabel("Year")
plt.ylabel("Number of Articles")
plt.title("Publications by Year")
plt.show()

# Identify top journals publishing COVID-19 research
print("Top journals publishing COVID-19 research:")
df.groupby('journal')['cord_uid'].count().sort_values(ascending=False).head(10).plot(kind='bar', figsize=(10, 6))
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Journal")
plt.ylabel("Number of Articles")
plt.show()

# Find the most frequent words in titles (simple word frequency)
print("Most frequent words in titles:")
df['title'].str.split().explode().value_counts().head(10).plot(kind='bar', figsize=(10, 6))
plt.title("Top 10 Most Frequent Words in Titles")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.show()

# Plot distribution of publications by source
print("Distribution of publications by source:")
df['source_x'].value_counts().plot(kind='bar', figsize=(10, 6))
plt.title("Distribution of Publications by Source")
plt.xlabel("Source")
plt.ylabel("Number of Articles")
plt.show()