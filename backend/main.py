from fastapi import FastAPI
from utils.stockedge import get_major_nse_indices, get_trending_stocks
from utils.news import money_control_news
from utils.nsedata import get_ohlc_data
import json

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/nse_indices/{period}")
async def nse_indices(period: str):
    if period in ["1D", "1W", "1M", "3M", "6M", "1Y", "2Y", "5Y"]:
        data = get_major_nse_indices(period)
    else:
        data = {
            "error": "invalid period should be within 1D, 1W, 1M, 3M, 6M, 1Y, 2Y, 5Y"
        }
    return data


@app.get("/trending_news")
async def trending_news():
    news_data = money_control_news()
    return news_data


@app.get("/nse")
async def nse_data():
    nse_data = get_ohlc_data("SBIN", "EQ")  
    return nse_data.to_csv()