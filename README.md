# 📚 Book Price Analysis  
A data-driven project by **Team DataCrafters**

## 📖 Project Overview  
This repository contains a data engineering and analysis project focused on extracting, cleaning, analyzing, and visualizing book data. The goal is to uncover patterns in **book prices, ratings, availability**, and **categories** using web scraping and public APIs.

We scrape data from:
- [Books to Scrape](https://books.toscrape.com)
- [OpenLibrary](https://openlibrary.org)
- [Google Books API](https://developers.google.com/books)

Our final product includes:
- Cleaned and enriched dataset
- Statistical and visual insights
- A ready-to-query SQL Server database
- *(Bonus)* A Streamlit app for interactive book comparison *(in progress)*

---

## 🛠️ Technologies Used

### 🐍 Programming Language:
- Python 3.9+

### 📚 Libraries:
- `requests`, `BeautifulSoup` – Web Scraping  
- `pandas`, `numpy` – Data Cleaning and Manipulation  
- `matplotlib`, `seaborn` – Visualization  
- `re` – Regular Expressions  
- `sqlalchemy`, `pyodbc` – SQL Server Integration  

### 🧰 Tools:
- Jupyter Notebook
- SQL Server (BooksDB)
- Streamlit *(for app development – planned)*

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/BookPriceAnalysis.git
cd BookPriceAnalysis

pip install -r requirements.txt

streamlit run app.py


