# 🧬 CORD-19 Data Explorer

## 📖 Task Description
This work is part of the **Python Assignment - Week 8**, whose goal is to practice the fundamental stages of the data science workflow — from data loading and cleaning to visualization and presentation through a **Streamlit** app.

The dataset used is **metadata.csv** from the **CORD-19 Research Dataset**, which contains information about scientific articles related to COVID-19.  
To simplify processing, only a sample of **5000 rows** and key columns was used.

---

## 🎯 Learning Objectives
With this project, it was possible to:

- Practice **loading and exploring** a real dataset.  
- Apply **basic data cleaning techniques**.  
- Generate **meaningful visualizations** to identify trends.  
- Build an **interactive Streamlit web app**.  
- Gain hands-on experience with the **complete data science workflow**.

---

## 🧰 Tools and Libraries Used
 _____________________________________________________________________
| Library        |                 Main Purpose                       |
|________________|____________________________________________________|
| **pandas**     | Data manipulation, cleaning, and tabular analysis  |
| **matplotlib** | Basic charting and visualization                   |
| **streamlit**  | Creating an interactive web app to display results |
|_____________________________________________________________________| 

## ⚙️ Project Steps

### 1. Data Loading and Exploration
- Loaded `metadata.csv` selecting specific columns (`title`, `abstract`, `publish_time`, `journal`, `authors`, `source_x`).
- Read only **5000 records** to improve performance.
- Inspected dataset dimensions, data types, and missing values.

### 2. Data Cleaning and Preparation
- Handled missing values by replacing nulls with placeholders (`No title`, `Unknown`, etc.).
- Removed duplicate entries based on title and publication date.
- Created a new column `year` derived from `publish_time`.
- Added a `word_count` column to measure abstract length.

### 3. Analysis and Visualization
Created visualizations using **matplotlib**:
- 📊 Publications per year.
- 🏛️ Top journals publishing COVID-19 research.
- 📝 Most frequent words in article titles.
- 🌍 Distribution of publications by source.

These visualizations help to understand **the evolution of scientific research** and **the main publication sources**.

### 4. Streamlit App
A simple app was built including:
- Title and project description.  
- Interactive **year range filter** (slider).  
- Display of visualizations directly in the app.  
- Sample of the dataset.  

The app offers a simple and intuitive way to explore analysis results.

---

## 📊 Key Findings
- The number of COVID-19-related publications **increased dramatically in 2020**.  
- Certain journals stood out as main sources of research.  
- The most frequent words in titles reflect central topic such as *Virus*.  

These findings illustrate the intense scientific production driven by the pandemic.

---

## 💡 Personal Reflection
Throughout this project, I learned the importance of **data preprocessing**, which is crucial before generating any visualization or insight.  
I also learned to use **Streamlit** as a simple yet powerful tool for turning analysis into interactive applications.  

The biggest challenge was managing the dataset size, requiring sampling and column selection.  
Overall, this work served as a great practical introduction to the **data science workflow**, combining Python, analysis, and visualization.

---

## 🚀 Running the Project
To run the app:

```bash
# Install dependencies
pip install pandas matplotlib streamlit seaborn

# Run the Streamlit app
streamlit run appStreamlit.py
```

---

## 📁 Project Structure
```
Frameworks_Assignment/
│
├── CORD19DataExplorer.py   # Main project script
├── appStreamlit.py         # Streamlit visualization app
├── metadata.csv            # Original dataset (not included in GitHub)
├── metadata_prepared.csv   # Cleaned dataset version
└── README.md               # Project documentation and reflection
```

---

**Author:** Garcia Damião  
**Course:** Power Learn Project — Python  
**Date:** October 2025  
