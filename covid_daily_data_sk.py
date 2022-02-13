import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

stats = pd.read_csv('OpenData_Slovakia_Covid_DailyStats.csv', delimiter=';')  #you can download recent data from health analytics institute https://github.com/Institut-Zdravotnych-Analyz/covid19-data/tree/main/DailyStats

stats['PCR posit. percentage'] = ((stats['Dennych.PCR.prirastkov'] / stats['Dennych.PCR.testov']).round(decimals=2)) * 100
stats['Datum'] = pd.to_datetime(stats['Datum'])

date = stats['Datum']
percentage = stats['PCR posit. percentage']
cases = stats['Dennych.PCR.prirastkov']

fig, ax = plt.subplots()

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
ax.figure.set_size_inches(18,6)
ax.plot(date, percentage, color = 'red')
ax.set_xlabel('date')
ax.set_ylabel('%', color = 'r')
ax.figure.autofmt_xdate(rotation=45, ha='center')
ax2 = ax.twinx()
ax2.plot(date, cases, color = 'blue')
ax2.set_ylabel('cases', color = 'b')

plt.show()

# See example plot for reference to see if script was executed correctly
