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

usa_daily_cases=usa['total_cases'].diff(1).fillna(0)
yesterday_cases=usa_daily_cases[-1]



print("********************************************************************************")


print(f"\nUSA TOTAL CASE COUNT: {sum(usa_daily_cases.fillna(0)):,} as of "+today.strftime("%A")+' '+str( today),"\n")

print(f"Most infectious day in USA history: {usa_daily_cases.max():,.0f}",usa_daily_cases.idxmax().strftime("%B, %d, %Y"),"\n" )


print(f"Yesterday's cases {today}: ",f"{yesterday_cases:,}\n")

print("Infections this week:")
print(usa_daily_cases.tail(14),"\n")


print("********************************************************************************")
