from us_stock import listStockInfoUS
from zh_stock import listStockInfoCN
from image_export import export

listStockInfoCN('H30269')
listStockInfoUS('.NDX')
listStockInfoUS('.INX')

export(source_file_name='H30269_近年数据.csv', buy_rate = - 0.07 ,sell_rate = 0.07)
export(source_file_name='.INX_近年数据.csv', buy_rate = - 0.1 ,sell_rate = 0.15)
export(source_file_name='.NDX_近年数据.csv', buy_rate = - 0.1 ,sell_rate = 0.15)