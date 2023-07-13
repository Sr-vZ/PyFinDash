from fastapi import FastAPI
from utils.stockedge import get_major_nse_indices, get_trending_stocks

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
