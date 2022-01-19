import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as datetime
from datetime import datetime as dt
import fetcher
today=dt.today()


fetcher.fetch()
print(f"LOCAL FETCH: world_{today.strftime('%b-%d-%Y')}.csv")
df = pd.read_csv(f"world_{today.strftime('%b-%d-%Y')}.csv",index_col='date', parse_dates=True)
print("LOCAL FETCH COMPLETE.")

usa=df[df['location'] == 'United States']
usa_daily_deaths=usa['total_deaths'].diff(1)
yesterday_deaths=usa_daily_deaths[-1]
usa_rolling7=usa_daily_deaths.rolling(7).mean()

print("********************************************************************************")

print(f"\nUSA TOTAL DEATH COUNT: {sum(usa_daily_deaths.fillna(0)):,} as of "+today.strftime("%A")+' '+str( today),"\n")

print(f"Deadliest day in USA history: {usa_daily_deaths.max():,.0f}",usa_daily_deaths.idxmax().strftime("%B, %d, %Y"),"\n" )


print(f"Yesterday's Deaths {today}: ",f"{yesterday_deaths:,}\n")

print("Deaths this week:")
print(usa_daily_deaths.tail(14),"\n")


print("********************************************************************************")

# FIG 1
fig = plt.figure(figsize=(15,8),dpi=200)
x1=usa['total_deaths'].diff(1)
ax=sns.lineplot(data=x1,x=x1.index,y=x1,color='#960056',label='Daily Deaths',lw=1,alpha=0.75)
ax=sns.lineplot(data=usa_rolling7, x=usa_rolling7.index,y=usa_rolling7,color='#ff000d',label='7 Day Average',lw=2.2)
ax.set_title('CUMULATIVE COVID-19 USA Daily Deaths')
ax.set_facecolor('xkcd:sea green')
ax.set_ylabel("Deaths")
ax.set_xlabel("Date")
plt.show()
# fig.savefig(f'{today}_covid_deaths_all.png',dpi=165, bbox_inches='tight')

# FIG 2
start=today-datetime.timedelta(weeks=52)
end=today
MA7=usa_rolling7.loc[start:]
fig = plt.figure(figsize=(15,7),dpi=200)
x1=usa['total_deaths'].loc[start:].diff(1)
ax=sns.lineplot(data=x1,x=x1.index,y=x1,color='#960056',lw=0.83,alpha=0.75, label='Daily Deaths')
ax=sns.lineplot(data=MA7, x=MA7.index,y=MA7,color='#ff000d',label='7 Day Average (Deaths)')
ax.set_title('12 MONTH ANALYSIS: Present ~ COVID-19 USA Daily Deaths')
ax.set_facecolor('xkcd:sea green')
ax.set_ylabel("Deaths")
ax.set_xlabel("Date")
plt.show()

# FIG 3
start=today-datetime.timedelta(weeks=4)
end=today
MA7=usa_rolling7.loc[start:]
fig = plt.figure(figsize=(15,7),dpi=200)
x1=usa['total_deaths'].loc[start:].diff(1)
ax=sns.lineplot(data=x1,x=x1.index,y=x1,color='#960056',lw=1.43,alpha=0.75, label='Daily Deaths')
ax=sns.lineplot(data=MA7, x=MA7.index,y=MA7,lw=2.66,color='#ff000d',label='7 Day Average (Deaths)')
ax.set_title('4 Week Analysis ~ COVID-19 USA Daily Deaths')
ax.set_facecolor('xkcd:sea green')
ax.set_ylabel("Deaths")
ax.set_xlabel("Date")
plt.show()

# fig.savefig(f'{today}_covid19_deaths.png',dpi=165, bbox_inches='tight')


print("end")