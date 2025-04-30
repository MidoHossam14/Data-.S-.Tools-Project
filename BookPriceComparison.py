import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set page config
st.set_page_config(page_title="Book Price Comparison Tool", layout="wide")

# Title and description
st.title("📚 Book Price Comparison Tool")
st.markdown("""
Compare book prices across multiple platforms to find the best deal!
""")

# Sidebar for user input
with st.sidebar:
    st.header("Search Parameters")
    book_title = st.text_input("Book Title", "The Great Gatsby")
    book_author = st.text_input("Author (optional)", "F. Scott Fitzgerald")
    search_button = st.button("Search Prices")

# Function to scrape Book to Scrape
def scrape_book_to_scrape(title, author=None):
    try:
        base_url = "https://books.toscrape.com"
        search_url = f"{base_url}/catalogue/search.html?q={title.lower().replace(' ', '+')}"
        
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        books = []
        for article in soup.find_all('article', class_='product_pod'):
            book_title = article.h3.a['title']
            price = article.find('p', class_='price_color').text
            availability = article.find('p', class_='instock availability').text.strip()
            
            books.append({
                'title': book_title,
                'price': price,
                'availability': availability,
                'source': 'Book to Scrape'
            })
        
        return books[:3]  # Return top 3 results
    except Exception as e:
        st.error(f"Error scraping Book to Scrape: {e}")
        return []

# Function to query Open Library
def query_open_library(title, author=None):
    try:
        base_url = "https://openlibrary.org/search.json"
        params = {'title': title}
        if author:
            params['author'] = author
            
        response = requests.get(base_url, params=params)
        data = response.json()
        
        books = []
        for doc in data.get('docs', [])[:3]:  # Limit to 3 results
            title = doc.get('title', 'N/A')
            authors = ", ".join(doc.get('author_name', ['Unknown']))
            published = doc.get('first_publish_year', 'N/A')
            isbn = doc.get('isbn', ['N/A'])[0] if doc.get('isbn') else 'N/A'
            
            # Open Library doesn't provide prices directly, so we'll indicate free access
            books.append({
                'title': title,
                'price': 'Free Access',
                'availability': 'Available',
                'authors': authors,
                'published': published,
                'isbn': isbn,
                'source': 'Open Library'
            })
        
        return books
    except Exception as e:
        st.error(f"Error querying Open Library: {e}")
        return []

# Function to query Google Books API
def query_google_books(title, author=None):
    try:
        base_url = "https://www.googleapis.com/books/v1/volumes"
        params = {'q': title, 'maxResults': 3}
        if author:
            params['q'] += f"+inauthor:{author}"
            
        response = requests.get(base_url, params=params)
        data = response.json()
        
        books = []
        for item in data.get('items', [])[:3]:  # Limit to 3 results
            volume_info = item.get('volumeInfo', {})
            sale_info = item.get('saleInfo', {})
            
            title = volume_info.get('title', 'N/A')
            authors = ", ".join(volume_info.get('authors', ['Unknown']))
            published = volume_info.get('publishedDate', 'N/A')
            isbn = volume_info.get('industryIdentifiers', [{}])[0].get('identifier', 'N/A')
            
            if sale_info.get('saleability') == 'FOR_SALE':
                price = f"{sale_info.get('retailPrice', {}).get('amount', 'N/A')} {sale_info.get('retailPrice', {}).get('currencyCode', '')}"
            else:
                price = sale_info.get('saleability', 'NOT_FOR_SALE').replace('_', ' ').title()
            
            books.append({
                'title': title,
                'price': price,
                'availability': 'Available' if sale_info.get('saleability') == 'FOR_SALE' else 'Not for sale',
                'authors': authors,
                'published': published,
                'isbn': isbn,
                'source': 'Google Books'
            })
        
        return books
    except Exception as e:
        st.error(f"Error querying Google Books: {e}")
        return []

# Main app logic
if search_button:
    with st.spinner("Searching for book prices..."):
        # Initialize results
        results = []
        
        # Scrape/query all sources
        bts_results = scrape_book_to_scrape(book_title, book_author)
        ol_results = query_open_library(book_title, book_author)
        gb_results = query_google_books(book_title, book_author)
        
        # Combine results
        results.extend(bts_results)
        results.extend(ol_results)
        results.extend(gb_results)
        
        # Display results
        if not results:
            st.warning("No results found. Try a different search term.")
        else:
            # Convert to DataFrame for better display
            df = pd.DataFrame(results)
            
            # Reorder columns for better display
            if 'authors' in df.columns:
                df = df[['title', 'authors', 'price', 'availability', 'source']]
            else:
                df = df[['title', 'price', 'availability', 'source']]
            
            # Display results in tabs
            tab1, tab2 = st.tabs(["Table View", "Card View"])
            
            with tab1:
                st.dataframe(df, use_container_width=True)
            
            with tab2:
                cols = st.columns(3)
                for idx, book in enumerate(results):
                    with cols[idx % 3]:
                        st.markdown(f"""
                        <div style="
                            border: 1px solid #ddd;
                            border-radius: 10px;
                            padding: 15px;
                            margin-bottom: 15px;
                            height: 250px;
                        ">
                            <h4>{book['title']}</h4>
                            <p><strong>Source:</strong> {book['source']}</p>
                            <p><strong>Price:</strong> {book['price']}</p>
                            <p><strong>Availability:</strong> {book['availability']}</p>
                            {'<p><strong>Author(s):</strong> ' + book.get('authors', 'N/A') + '</p>' if 'authors' in book else ''}
                        </div>
                        """, unsafe_allow_html=True)
            
            # Add some metrics
            st.subheader("Price Summary")
            col1, col2, col3 = st.columns(3)
            
            # Count available prices
            price_count = sum(1 for book in results if isinstance(book['price'], str) and 'free' not in book['price'].lower() and 'N/A' not in book['price'])
            
            col1.metric("Total Results", len(results))
            col2.metric("Sources Queried", 3)
            col3.metric("Available Prices", price_count)

# Add some info when the page first loads
if not search_button:
    st.info("""
    **How to use this tool:**
    1. Enter a book title (and optionally author) in the sidebar
    2. Click the "Search Prices" button
    3. Compare prices across different platforms
    
    **Note:** Some platforms may not return prices but provide free access to books.
    """)
    
    # Show sample data
    st.subheader("Sample Comparison")
    sample_data = [
        {"title": "The Great Gatsby", "source": "Book to Scrape", "price": "£12.99", "availability": "In stock"},
        {"title": "The Great Gatsby", "source": "Open Library", "price": "Free Access", "availability": "Available"},
        {"title": "The Great Gatsby", "source": "Google Books", "price": "9.99 USD", "availability": "Available"},
    ]
    st.dataframe(pd.DataFrame(sample_data), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
*Data is collected from multiple sources and may not be 100% accurate or up-to-date.*
""")