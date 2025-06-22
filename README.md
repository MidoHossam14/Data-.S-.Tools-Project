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

## How to Use and Run

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/MidoHossam14/Data-.S-.Tools-Project.git
   cd FULL-PROJECT
2. **Install Dependencies**:

    Ensure you have Python installed (recommended: `Python 3.9`). Install the required libraries using:

    ```bash
    pip install -r requirements.txt
3. **Run Jupyter Notebooks**:

    Navigate to the `notebooks` folder and launch Jupyter:

    ```bash
    jupyter notebook
3. **Run Streamlit App**:

    Navigate to the `notebooks` folder and launch Jupyter:

    ```bash
    streamlit run app.py

- Open the desired notebook and execute the cells to run the code.
##  📂 Repository Structure

 ```txt
📦 BookPriceAnalysis/
 ┣ 📜BooksPriceAnalysis.ipynb         ← Main analysis notebook
 ┣ 📜BookPriceComparison.py           ← Streamlit app for book search & comparison
 ┣ 📜books.csv                        ← Raw merged dataset
 ┣ 📜books_data_cleaned.csv           ← Cleaned dataset
 ┣ 📜Booksdb.sql                      ← SQL Server database schema
 ┣ 📜FinalReport.docx                 ← Project final report
 ┣ 📜ProjectDetails.docx              ← Project requirements
 ┣ 📜DS_Final_Project.pdf             ← PDF version of project
 ┣ 📜LICENSE                          ← MIT License
 ┣ 📜README.md                        ← You’re reading it now
 ┗ 📜file_version.ssmssl              ← Auto-saved state (can be ignored)
```


## 📊 Project Highlights
  ✅ Web scraping from 3 diverse sources

  ✅ Regex-based data cleaning and standardization

  ✅ Descriptive statistics on price & rating trends

  ✅ Visualizations for top categories, pricing patterns, and source comparisons

  ✅ Data pushed to SQL Server for structured storage

  🟡 (In progress): Streamlit app for interactive querying & book comparison

  
## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/MidoHossam14/Data-.S-.Tools-Project/blob/main/LICENSE) file for details.


## ☕ Stay Connected
Let's stay in touch! Feel free to connect with us :
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohamed-gehad-82a726329/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohammed-hossam-6047ab30b/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohamed-yasser-5a56672ab/i)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohamed-ahmed-547420326/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohamed-ayman-52053328a/)



