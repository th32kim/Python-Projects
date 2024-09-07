from datetime import datetime
import calendar
today = datetime.today().strftime('%m-%d-%Y').split('-')
month = calendar.month_name[int(today[0])]
print(f'{month} {today[1]}, {today[2]}')