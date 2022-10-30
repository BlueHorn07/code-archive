import pandas as pd
import matplotlib.pyplot as plt

"""
Matlab-style Usage. (OOP-style is recommended instead of this)
Lack of functionality compare to OOP-style.
Use `plt.plot()` and `plt.subplot()`.
"""

def plot_timeseries(datetime, value):
  fig_w = 16
  fig_h = 4
  plt.figure(figsize=(fig_w, fig_h), facecolor='white')

  plt.plot(datetime, value)

  plot_title = 'Time Series Plot'
  plt.title(plot_title)

  plt.grid()
  plt.show()

def plot_multiple_timeseries(
  col: int, row: int, 
  datetime_list: list,
  value_list: list, 
  title_list: list
):
  fig_w = 20
  fig_h = 8
  plt.figure(figsize=(fig_w, fig_h), facecolor='white')

  for idx in range(len(datetime_list)):
    datetime = datetime_list[idx]
    value = value_list[idx]
    title = title_list[idx]

    plt.subplot(row, col, idx + 1)
    plt.plot(datetime, value)
    plt.title(title)
    plt.grid()
  
  plt.show()


csv_url = 'https://raw.githubusercontent.com/ejgao/Time-Series-Datasets/master/monthly-beer-production-in-austr.csv'
df = pd.read_csv(csv_url)

datetime_col = 'Month'
value_col = 'Monthly beer production'
df[datetime_col] = pd.to_datetime(df[datetime_col])

plot_timeseries(df[datetime_col], df[value_col])

plot_multiple_timeseries(
  col = 2, 
  row = 2, 
  datetime_list = [df[datetime_col], df[datetime_col], df[datetime_col], df[datetime_col]],
  value_list = [df[value_col], df[value_col], df[value_col], df[value_col]],
  title_list = ["a", "b", "c", "d"]
)