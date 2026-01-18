# -*- coding: utf-8 -*-
import akshare as ak
from stock_const import data_dir 

def listStockInfoUS(symbol):
    df = ak.index_us_stock_sina(symbol=symbol)
    # 只保留需要的列
    df = df[['date', 'close', 'open']]
    df = df.sort_values('date').reset_index(drop=True)
    df.to_csv(f"{data_dir}/{symbol}_近年数据.csv", index=False, encoding="utf-8-sig")
