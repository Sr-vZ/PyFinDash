import requests

price_change_period = [1, 7, 30, 90, 180, 365, 730, 1825]


# Define a list of user agents to rotate through
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.133 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
]


def get_major_nse_indices(period="1D"):
    """
    Valid periods are 1D, 1W, 1M, 3M, 6M, 1Y, 2Y, 5Y
    default is 1D
    """

    price_change_period = {
        "1D": 1,
        "1W": 7,
        "1M": 30,
        "3M": 90,
        "6M": 180,
        "1Y": 365,
        "2Y": 730,
        "5Y": 1825,
    }
    major_nse_index = (
        "https://api.stockedge.com/Api/DailyDashboardApi/GetLatestIndexQuotes?exchange=NSE&priceChangePeriodType="
        + str(price_change_period[period])
        + "&lang=en"
    )
    res = requests.get(major_nse_index)
    # print(res.json())
    return res.json()


def get_trending_stocks(segment="Major", gain_loss="gain"):
    segment_options = {
        "Nifty50": "8",
        "Nifty200": "11",
        "Major": "10",
    }
    gain_loss_option = {"gain": "1", "loss": "2"}

    trending_stocks_url = f"https://api.stockedge.com/Api/trendingstocksapi/GetPriceMovers?relevantListings={segment_options[segment]}&gainerLosersTypeEnum={gain_loss_option[gain_loss]}&page=1&pageSize=10&lang=en"
    res = requests.get(trending_stocks_url)

    return res.json()


# print(get_major_nse_indices())
# print(get_trending_stocks())
