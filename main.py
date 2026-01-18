from stock_us import listStockInfoUS
from stock_zh import listStockInfoCN
from image_export import export

years = 1
listStockInfoCN(symbol='512890', days=years * 365)
listStockInfoUS('.NDX')
listStockInfoUS('.INX')

export(source_file_name='512890_近年数据.csv', buy_rate = - 0.07, sell_rate = 0.07, years=years)
export(source_file_name='.INX_近年数据.csv', buy_rate = - 0.1, sell_rate = 0.15, years=years)
export(source_file_name='.NDX_近年数据.csv', buy_rate = - 0.1, sell_rate = 0.15, years=years)