import pandas as pd
import datetime as datetime
from datetime import datetime as dt
import os
today=dt.today()

def usa_force_fetch():
    print("Force Fetch initiating... \nCreating...\n..............\n..............\n..............")
    data_path= 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'
    df = pd.read_csv(data_path)
    df.to_csv(f"usa_{today.strftime('%b-%d-%Y')}.csv")
    print(f"CREATED: usa_{today.strftime('%b-%d-%Y')}.csv")

if __name__ == "__main__":
    usa_force_fetch()


