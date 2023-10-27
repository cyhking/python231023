import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EB%A7%A5%EB%B6%81"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements that contain the information you want
    blog_list = soup.find_all('li', class_='sh_blog_top')

    for blog in blog_list:
        # Extract blog name
        blog_name = blog.find('a', class_='sh_blog_title').text

        # Extract blog address
        blog_url = blog.find('a', class_='sh_blog_title')['href']

        # Extract post title
        post_title = blog.find('a', class_='sh_blog_title')['title']

        # Extract date
        date = blog.find('dd', class_='txt_inline').text

        # Print the information
        print(f"Blog Name: {blog_name}")
        print(f"Blog Address: {blog_url}")
        print(f"Post Title: {post_title}")
        print(f"Date: {date}")
        print("\n")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
