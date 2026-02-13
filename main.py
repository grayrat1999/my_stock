from stock_us import listStockInfoUS
from stock_zh import listETFInfoCN
from image_export import export


class QueryParam:
    def __init__(self, symbol, buy_rate, sell_rate):
        self.symbol = symbol
        self.buy_rate = buy_rate
        self.sell_rate = sell_rate

def queryETF(params):
    years = 1
    for param in params:
        listETFInfoCN(symbol=param.symbol, days=years * 365)
        export(source_file_name=f'{param.symbol}_近年数据.csv', buy_rate=param.buy_rate, sell_rate=param.sell_rate, years=years)

def queryIndexUs(params):
    years = 1
    for param in params:
        listStockInfoUS(symbol=param.symbol)
        export(source_file_name=f'{param.symbol}_近年数据.csv', buy_rate=param.buy_rate, sell_rate=param.sell_rate, years=years)

queryETF([
        # 医药ETF
        QueryParam(symbol='159929', buy_rate=-0.07, sell_rate=0.07),
        # 恒生科技ETF
        QueryParam(symbol='513010', buy_rate=-0.07, sell_rate=0.07),
        # 消费ETF
        QueryParam(symbol='159798', buy_rate=-0.07, sell_rate=0.07),
        # 港股低波红利ETF摩根
        QueryParam(symbol='513630', buy_rate=-0.07, sell_rate=0.07),
        # 红利ETF易方达
        QueryParam(symbol='515180', buy_rate=-0.07, sell_rate=0.07),
        # 道琼斯ETF
        QueryParam(symbol='513400', buy_rate=-0.07, sell_rate=0.07),
        # 日经ETF
        QueryParam(symbol='513000', buy_rate=-0.07, sell_rate=0.07),
])

queryIndexUs([
    # 标普
    QueryParam(symbol='.INX', buy_rate=-0.1, sell_rate=0.15),
    # 纳指
    QueryParam(symbol='.NDX', buy_rate=-0.1, sell_rate=0.15),
])
