import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def export(source_file_name, buy_rate,sell_rate):
    df = pd.read_csv(f"{source_file_name}", encoding="utf-8-sig")
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values("date").reset_index(drop=True)

    # 计算1年滚动均值（252 个交易日）
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(365)).strftime("%Y-%m-%d")
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)].reset_index(drop=True)
    df['rolling_mean'] = df['close'].rolling(window=252, min_periods=1).mean()

    # 计算买入卖出阈值
    df['buy_price'] = df['rolling_mean'] * (1 + buy_rate)
    df['sell_price'] = df['rolling_mean'] * (1 + sell_rate)

    # 标记买入/卖出信号
    df['buy_signal'] = df['close'] <= df['buy_price']
    df['sell_signal'] = df['close'] >= df['sell_price']

    # 可视化
    plt.figure(figsize=(14,7))
    # 收盘价
    plt.plot(df['date'], df['close'], label='Close', color='blue')
    # 1 年均值
    plt.plot(df['date'], df['rolling_mean'], label='1Y Rolling Mean', color='orange', linestyle='--')
    # 买卖阈值
    plt.plot(df['date'], df['buy_price'], label=f'Buy Threshold ({buy_rate})', color='green', linestyle=':')
    plt.plot(df['date'], df['sell_price'], label=f'Sell Threshold ({sell_rate})', color='red', linestyle=':')
    # 买卖信号
    plt.scatter(df['date'][df['buy_signal']], df['close'][df['buy_signal']],
                marker='^', color='blue', label='Buy Signal', s=100)
    plt.scatter(df['date'][df['sell_signal']], df['close'][df['sell_signal']],
                marker='v', color='red', label='Sell Signal', s=100)

    plt.title(source_file_name.partition("_")[0])
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()


