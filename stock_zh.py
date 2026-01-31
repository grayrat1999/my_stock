# -*- coding: utf-8 -*-
import akshare as ak
from datetime import datetime, timedelta
from stock_const import data_dir 

def listIndexInfoCN(symbol, days=365):
    end_dt = datetime.today()
    start_dt = end_dt - timedelta(days)
    # 获取历史指数日线数据
    df = ak.index_zh_a_hist(
        symbol=symbol,
        period='daily',
        start_date=start_dt.strftime("%Y%m%d"),
        end_date=end_dt.strftime("%Y%m%d")
    )

    # 只保留需要的列
    df = df[["日期", "开盘", "收盘"]]
    # 改列名为英文
    df.columns = ["date", "open", "close"]
    df = df.sort_values("date")
    df.to_csv(f"{data_dir}/{symbol}_近年数据.csv", index=False, encoding="utf-8-sig")


def listETFInfoCN(symbol, days=365):
    end_dt = datetime.today()
    start_dt = end_dt - timedelta(days)

    # 获取 ETF 日线行情（东方财富）
    df = ak.fund_etf_hist_em(
        symbol=symbol,
        period="daily",
        start_date=start_dt.strftime("%Y%m%d"),
        end_date=end_dt.strftime("%Y%m%d"),
        adjust=""
    )
    df = df[["日期", "开盘", "收盘"]]
    df.columns = ["date", "open", "close"]
    df = df.sort_values("date")
    df.to_csv(
        f"{data_dir}/{symbol}_近年数据.csv",
        index=False,
        encoding="utf-8-sig"
    )
