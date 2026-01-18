from stock_us import listStockInfoUS
from stock_zh import listStockInfoCN
from stock_hk import listStockInfoHK
from image_export import export

listStockInfoCN('159525')
listStockInfoHK('513630')
listStockInfoUS('.NDX')
listStockInfoUS('.INX')

export(source_file_name='159525_近年数据.csv', buy_rate = - 0.07 ,sell_rate = 0.07)
export(source_file_name='513630_近年数据.csv', buy_rate = - 0.07 ,sell_rate = 0.07)
export(source_file_name='.INX_近年数据.csv', buy_rate = - 0.1 ,sell_rate = 0.15)
export(source_file_name='.NDX_近年数据.csv', buy_rate = - 0.1 ,sell_rate = 0.15)