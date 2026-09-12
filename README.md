# 🎬 Netflix Content Analysis & Recommendation System

A Data Science project that analyzes Netflix Movies and TV Shows and provides content-based recommendations using Machine Learning techniques.

---

## 📌 Project Overview

This project uses the Netflix Movies and TV Shows dataset to perform an end-to-end Data Science workflow.

The project includes:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Content-Based Recommendation System

The recommendation system suggests movies or TV shows that are similar to a title selected by the user.

---

## 🎯 Project Objective

The main objectives of this project are:

1. Clean and preprocess Netflix content data.
2. Analyze Netflix Movies and TV Shows.
3. Identify useful patterns and trends in the dataset.
4. Create meaningful features from the raw data.
5. Build a recommendation system that suggests similar content.
6. Understand how Machine Learning can be applied to recommendation systems.

---

## 🗂️ Dataset

The project uses a Netflix Movies and TV Shows dataset in CSV format.

### Important Columns

| Column | Description |
|---|---|
| `show_id` | Unique ID of the content |
| `type` | Movie or TV Show |
| `title` | Name of the content |
| `director` | Director of the content |
| `cast` | Cast members |
| `country` | Country where the content was produced |
| `date_added` | Date when content was added |
| `release_year` | Original release year |
| `rating` | Content rating |
| `duration` | Movie duration or number of seasons |
| `listed_in` | Genre/category |
| `description` | Description of the content |

---

# 🔄 Project Workflow

## 1. Data Collection

The Netflix dataset is collected in CSV format and stored as the raw dataset.

The original dataset is kept unchanged so that it can always be used again if required.

---

## 2. Data Cleaning

The raw dataset contains missing values and inconsistent data.

Data cleaning includes:

- Identifying missing values
- Removing or handling null values
- Checking duplicate records
- Converting columns into appropriate data types
- Cleaning date and duration information

### Example

```python
df = pd.read_csv("netflix.csv")

df_cleaned = df.dropna()

df_cleaned.to_csv("cleaned_netflix.csv", index=False)
