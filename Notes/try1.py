import requests 
from bs4 import BeautifulSoup

url = input("Enter the path:")


response = requests.get(url)
soup = BeautifulSoup(response.txt,"html.parse")

for link in soup.find_all("a"):
    print(link)

