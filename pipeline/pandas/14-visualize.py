#!/usr/bin/env python3
'''
My module document
'''

df = df.rename(columns={"Timestamp": "Date"})
df["Date"] = pd.to_datetime(df['Date'], unit='s')
df = df[df["Date"] >= pd.Timestamp('2017-01-01')]
df = df.set_index("Date")

df = df.drop(columns=["Weighted_Price"])

df['Close'] = df['Close'].ffill()
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

df = df.resample("D")

df = df.agg(func={
    "High": "max", 
    "Low": "min",
    "Open": 'mean',
    "Close": "mean",
    "Volume_(BTC)": "sum",
    "Volume_(Currency)": "sum"
    })

df.plot(kind="line")
