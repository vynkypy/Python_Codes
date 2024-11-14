
# import requests
# import json

# # Your NewsAPI key
# api_key = '15092d701ed64d0eb01a16e95554c267'
# url = 'https://newsapi.org/v2/top-headlines'
# parameters = {
#     'country': 'us',         # Example parameter
#     'apiKey': api_key
# }

# response = requests.get(url, params=parameters)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()  # Convert response to JSON
    
#     # Pretty-print the JSON to see all fields and structure
#     print(json.dumps(data, indent=4))
# else:
#     print("Error:", response.status_code, response.text)



# import requests
# import pandas as pd

# # Replace 'YOUR_API_KEY' with your actual NewsAPI key
# api_key = '15092d701ed64d0eb01a16e95554c267'
# url = 'https://newsapi.org/v2/top-headlines'
# parameters = {
#     'country': 'ind',         # Retrieve headlines from the US
#     'category': 'technology', # Category to filter by (e.g., business, sports, technology)
#     'apiKey': api_key
# }

# # Step 1: Make the request
# response = requests.get(url, params=parameters)

# # Step 2: Check if the request was successful
# if response.status_code == 200:
#     data = response.json()  # Parse the response JSON
    
#     # Step 3: Extract articles
#     articles = data.get('articles', [])
    
#     # Step 4: Create a DataFrame
#     df = pd.DataFrame(articles)
    
#     # Optional: Select specific columns
#     if not df.empty:
#         df = df[['source', 'author', 'title', 'description', 'url', 'publishedAt', 'content']]
#         df['source'] = df['source'].apply(lambda x: x['name'])  # Extract the source name
    
#     # Step 5: Save to CSV
#     df.to_csv('news_headlines_ind.csv', index=False)
#     print("Data successfully saved to news_headlines.csv")
# else:
#     print("Error fetching data:", response.status_code, response.text)


# import requests
# import pandas as pd

# # Replace 'YOUR_API_KEY' with your actual NewsAPI key
# api_key = '15092d701ed64d0eb01a16e95554c267'
# url = 'https://newsapi.org/v2/top-headlines'
# parameters = {
#     'country': 'us',          # Retrieve headlines from India (use 'in' for India)
#     'category': 'technology', # Category to filter by (e.g., business, sports, technology)
#     'apiKey': api_key,
#     'pageSize': 100,          # Increase the number of records (up to 100)
#     'page': 1                 # Specify the page number (if there are more articles, you can iterate through pages)
# }

# # Step 1: Make the request
# response = requests.get(url, params=parameters)

# # Step 2: Check if the request was successful
# if response.status_code == 200:
#     data = response.json()  # Parse the response JSON
    
#     # Step 3: Extract articles
#     articles = data.get('articles', [])
    
#     # Step 4: Create a DataFrame
#     df = pd.DataFrame(articles)
    
#     # Optional: Select specific columns
#     if not df.empty:
#         df = df[['source', 'author', 'title', 'description', 'url', 'publishedAt', 'content']]
#         df['source'] = df['source'].apply(lambda x: x['name'])  # Extract the source name
    
#     # Step 5: Save to CSV
#     df.to_csv('news_headlines_india.csv', index=False)
#     print(f"Data successfully saved to news_headlines_india.csv with {len(df)} records.")
# else:
#     print("Error fetching data:", response.status_code, response.text)


import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual NewsAPI key
api_key = '15092d701ed64d0eb01a16e95554c267'
url = 'https://newsapi.org/v2/top-headlines'

parameters = {
    'country': 'us',          # Retrieve headlines from India
    'category': 'technology',    # Broad category for more results
    'apiKey': api_key,
    'pageSize': 100,          # Maximum results per page
}

all_articles = []  # List to hold all articles

# Fetch results across multiple pages
for page in range(1, 6):  # Set the number of pages to retrieve, for example, 5 pages
    parameters['page'] = page
    response = requests.get(url, params=parameters)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the response JSON
        articles = data.get('articles', [])
        
        if articles:
            all_articles.extend(articles)  # Add the articles from the current page to the list
            print(f"Fetched {len(articles)} articles from page {page}")
        else:
            print(f"No articles found on page {page}")
    else:
        print(f"Error fetching data from page {page}: {response.status_code}")
        break  # Stop if there's an error fetching data

# Create a DataFrame if articles were fetched
if all_articles:
    df = pd.DataFrame(all_articles)
    
    # Optional: Select specific columns
    df = df[['source', 'author', 'title', 'description', 'url', 'publishedAt', 'content']]
    df['source'] = df['source'].apply(lambda x: x['name'])  # Extract the source name
    
    # Save to CSV
    df.to_csv('news_headlines_india.csv', index=False)
    print(f"Data successfully saved to news_headlines_india.csv with {len(df)} records.")
else:
    print("No articles were fetched.")
