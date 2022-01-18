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

# sigma_cases=sum(usa_daily.fillna(0))
print("**********************DEATHS***************************************************")
print(f"\nUSA TOTAL DEATH COUNT: {sum(usa_daily_deaths.fillna(0)):,} as of "+today.strftime("%A")+' '+str( today),"\n")

print(f"Deadliest day in USA history: {usa_daily_deaths.max():,.0f}",usa_daily_deaths.idxmax().strftime("%B, %d, %Y"),"\n" )


print(f"Yesterday's Deaths {today}: ",f"{yesterday_deaths:,}\n")

print("Deaths this week:")
print(usa_daily_deaths.tail(14),"\n")


print("**********************CASES**************************************************")
usa_daily_cases=usa['total_cases'].diff(1).fillna(0)
yesterday_cases=usa_daily_cases[-1]

print(f"\nUSA TOTAL CASE COUNT: {sum(usa_daily_cases.fillna(0)):,} as of "+today.strftime("%A")+' '+str( today),"\n")

print(f"Most infectious day in USA history: {usa_daily_cases.max():,.0f}",usa_daily_cases.idxmax().strftime("%B, %d, %Y"),"\n" )

print(f"Yesterday's cases {today}: ",f"{yesterday_cases:,}\n")

print("Infections this week:")
print(usa_daily_cases.tail(14),"\n")
