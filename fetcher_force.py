import pandas as pd
import datetime as datetime
from datetime import datetime as dt
import os
today=dt.today()

def force_fetch():
    start_time=dt.now()
    print("Force Fetch initiating... \nCreating...\n..............\n..............\n..............")
    data_path='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    df = pd.read_csv(data_path,index_col='date', parse_dates=True)
    df.to_csv(f"world_{today.strftime('%b-%d-%Y')}.csv")
    print(f"CREATED: world_{today.strftime('%b-%d-%Y')}.csv")
    end_time=dt.now()
    final_time=end_time-start_time
    print("Time Elapsed: ", final_time, " seconds")
if __name__ == "__main__":
    force_fetch()


