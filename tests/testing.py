import requests
from bs4 import BeautifulSoup
import re

url = "https://www.google.com/finance/"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")
# headlines = soup.find("body").find_all("data-article-source-name")
# for x in headlines:
#     print(x.text.strip())


# mc_econ_news = "https://www.moneycontrol.com/news/business/economy/"

# response = requests.get(mc_econ_news)
# # print(response.text)
# soup = BeautifulSoup(response.text, "html.parser")
# news_divs = soup.find("body").find_all(id=re.compile("^newslist-"))

# for nd in news_divs:
#     h = nd.find("h2").text.strip()
#     d = nd.find("span").text.strip()
#     p = nd.find("p").text.strip()
#     print(f"{d}\t{h}\t{p}")

nse_url = "https://www.nseindia.com/"

# Set the user-agent header to mimic a web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Make the request to the URL with headers
# response = requests.get(nse_url, headers=headers)
# print(response.text)
# soup = BeautifulSoup(response.text, "html.parser")
# table = soup.find(id="tab1Ganier")

# print(table)
