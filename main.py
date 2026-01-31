from stock_us import listStockInfoUS
from stock_zh import listIndexInfoCN, listETFInfoCN
from image_export import export

years = 1

# 港股低波红利ETF摩根
listETFInfoCN(symbol='513630', days=years * 365)
export(source_file_name='513630_近年数据.csv', buy_rate = - 0.07, sell_rate = 0.07, years=years)

# 红利ETF易方达
listETFInfoCN(symbol='515180', days=years * 365)
export(source_file_name='515180_近年数据.csv', buy_rate = - 0.07, sell_rate = 0.07, years=years)

# 医药ETF
listETFInfoCN(symbol='159929', days=years * 365)
export(source_file_name='159929_近年数据.csv', buy_rate = - 0.07, sell_rate = 0.07, years=years)

# 恒生科技ETF
listETFInfoCN(symbol='513010', days=years * 365)
export(source_file_name='513010_近年数据.csv', buy_rate = - 0.07, sell_rate = 0.07, years=years)

# 标普
listStockInfoUS('.INX')
export(source_file_name='.INX_近年数据.csv', buy_rate = - 0.1, sell_rate = 0.15, years=years)

# 纳指
listStockInfoUS('.NDX')
export(source_file_name='.NDX_近年数据.csv', buy_rate = - 0.1, sell_rate = 0.15, years=years)