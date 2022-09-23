import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

"""
OOP-style Usage. 
Use `plt.subplots()`.
"""

def plot_timeseries(datetime, value):
  fig_w = 16
  fig_h = 4
  fig, ax = plt.subplots(figsize=(fig_w, fig_h))
  fig.patch.set_facecolor('white')

  ax.plot(pd.to_datetime(datetime), value)

  fig_title = 'Time Series Plot'
  plt.title(fig_title)

  # formatting
  fig.autofmt_xdate()
  ax.xaxis.set_major_locator(mdates.YearLocator())
  ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
  ax.xaxis.set_minor_locator(mdates.MonthLocator())
  # ax.xaxis.set_minor_formatter(mdates.DateFormatter('%m'))
  ax.grid()

  plt.show()


def plot_multiple_timeseires(
  col: int, row: int, 
  datetime_list: list,
  value_list: list, 
  title_list: list
):
  fig_w = 20
  fig_h = 8
  fig, axes = plt.subplots(col, row, figsize=(fig_w, fig_h))
  fig.patch.set_facecolor('white')

  for i in range(col):
    for j in range(row):
      ax = axes[i][j]
      datetime = datetime_list[i * col + j]
      value = value_list[i * col + j]
      title = title_list[i * col + j]

      ax.plot(datetime, value)
      
      ax.set_title(title)

      # formatting
      fig.autofmt_xdate()
      ax.xaxis.set_major_locator(mdates.YearLocator())
      ax.xaxis.set_minor_locator(mdates.MonthLocator())
      ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
      # ax.xaxis.set_minor_formatter(mdates.DateFormatter('%m'))
      ax.grid()
  
  plt.show()


csv_url = 'https://raw.githubusercontent.com/ejgao/Time-Series-Datasets/master/monthly-beer-production-in-austr.csv'
df = pd.read_csv(csv_url)

datetime_col = 'Month'
value_col = 'Monthly beer production'
df[datetime_col] = pd.to_datetime(df[datetime_col])

plot_timeseries(df[datetime_col], df[value_col])

plot_multiple_timeseires(
  col = 2, 
  row = 2, 
  datetime_list = [df[datetime_col], df[datetime_col], df[datetime_col], df[datetime_col]],
  value_list = [df[value_col], df[value_col], df[value_col], df[value_col]],
  title_list = ["a", "b", "c", "d"]
)