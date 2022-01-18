import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid",{"axes.facebolor":"0.90"})
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth":2.5})

#time_series_covid19_deaths_US.csv
# jhu_deaths_state='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'
# df = pd.read_csv(jhu_deaths_state)
# df.to_csv("jhu_usa.csv")
df=pd.read_csv("jhu_usa.csv")

# del df['UID']
# del df['iso2']
# del df['iso3']
# del df['code3']
# del df['FIPS']
# del df['Combined_Key']
# del df['Lat'] 
# del df['Long_']

# #video got rid of all non-date columns
# # Province_State	Country_Region	Population
# del df['Province_State']
# del df['Country_Region']
# del df['Population']

df.set_index("Admin2",inplace=True)

from datetime import datetime

datetime.today().month, datetime.today().day, datetime.today().year

today_col = str(datetime.today().month)+'/' +str(datetime.today().day)+'/'+ str(datetime.today().year)[:-2]

from datetime import datetime
today=datetime.today()