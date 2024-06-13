import requests
from nsepython import nse_eq

def get_ltp(symbol):
    ltp = nse_eq(symbol)
    return ltp
    


