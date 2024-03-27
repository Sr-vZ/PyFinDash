from nsepython import *

def get_ohlc_data(symbol, series, start_date=None, end_date=None):
    if symbol == None:
        return None
    if series == None:
        series = "EQ"
    
    if (end_date == None):
        end_date = datetime.datetime.now().strftime("%d-%m-%Y")
        end_date = str(end_date)
    
    if (start_date == None):
        start_date = (datetime.datetime.now()- datetime.timedelta(days=65)).strftime("%d-%m-%Y")
        start_date = str(start_date)
    
    df = equity_history(symbol, series, start_date, end_date)
    
    return df