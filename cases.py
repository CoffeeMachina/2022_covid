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

usa_rolling7=usa['total_cases'].diff(1).fillna(0).rolling(7).mean()
usa_daily_cases=usa['total_cases'].diff(1).fillna(0)
yesterday_cases=usa_daily_cases[-1]



print("********************************************************************************")


print(f"\nUSA TOTAL CASE COUNT: {sum(usa_daily_cases.fillna(0)):,} as of "+today.strftime("%A")+' '+str( today),"\n")

print(f"Most infectious day in USA history: {usa_daily_cases.max():,.0f}",usa_daily_cases.idxmax().strftime("%B, %d, %Y"),"\n" )


print(f"Yesterday's cases {today}: ",f"{yesterday_cases:,}\n")

print("Infections this week:")
print(usa_daily_cases.tail(14),"\n")

print("7-Day MA:")
print(usa_rolling7.tail(14),"\n")


print("********************************************************************************")

#FIG 1
start=today-datetime.timedelta(weeks=12)
end=today
MA7=usa_rolling7.loc[start:]
fig = plt.figure(figsize=(15,7),dpi=200)
plt.ticklabel_format(style='plain', axis='y')

x1=usa_daily_cases.loc[start:]
ax=sns.lineplot(data=x1,x=x1.index,y=x1,color='#960056',label='Daily Cases')
ax=sns.lineplot(data=MA7, x=MA7.index,y=MA7,color='#ff000d',label='7 Day Case Average')
ax.set_title('3 Months: COVID-19 USA Daily Cases')
ax.set_facecolor('xkcd:aquamarine')
ax.set_ylabel("Cases")
ax.set_xlabel("Date")
plt.show()
