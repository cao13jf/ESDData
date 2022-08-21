import pandas as pd
from datetime import datetime

date_file = "./date.csv"
pd_date = pd.read_csv(date_file, header=None)
date_strs = pd_date[0].tolist()
all_dates = []
data_strs = []
for date_str in date_strs:
    str_date = date_str.split(":")[-1].lstrip()
    print(str_date)
    data_strs.append(str_date)
    date_obj = datetime.strptime(str_date, '%d/%m/%Y')
    all_dates.append(date_obj)

start_date = all_dates[0]
till_now_days = [0]
for end_date in all_dates[1:]:
    detla = (end_date - start_date).days
    till_now_days.append(detla)

till_now_days = [x + 1 for x in till_now_days]
date_dict = {"Rank": list(range(1, len(till_now_days) + 1, 1)), "Date": data_strs, "Days": till_now_days}
pd_date = pd.DataFrame.from_dict(date_dict)
pd_date.to_csv("./case_date_days.csv", index=False)

