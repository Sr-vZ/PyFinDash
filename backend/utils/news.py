import requests
from bs4 import BeautifulSoup
import re
import random


# Define a list of user agents to rotate through
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.133 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
]


# # Send a GET request to the URL and parse the response with BeautifulSoup
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all the news headlines on the page
# headlines = soup.find_all("h2", class_="headline")

# # Print each headline
# for headline in headlines:
#     print(headline.get_text().strip())


def money_control_news():
    # Define the URL to scrape
    url = "https://www.moneycontrol.com/news/economy/"

    # Choose a random user agent from the list for each request
    headers = {"User-Agent": random.choice(user_agents)}

    # Send a GET request to the URL and parse the response with BeautifulSoup
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    news_divs = soup.find("body").find_all(id=re.compile("^newslist-"))

    json_op = []
    for nd in news_divs:
        h = nd.find("h2").text.strip()
        d = nd.find("span").text.strip()
        p = nd.find("p").text.strip()
        json_op.append({"date": d, "title": h, "description": p})
        # print(f"{d}\t{h}\t{p}")

    return json_op


print(money_control_news())
