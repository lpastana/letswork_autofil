import time
import argparse
from browser import Browser

parser = argparse.ArgumentParser(description='Letswork timesheet autofil system')

parser.add_argument('-s', '--start-date', type=str, help='Start date in format dd-mm-yyyy')
parser.add_argument('-e', '--end-date', type=str, help='End date in format dd-mm-yyyy')
parser.add_argument('-t', '--today', help='Fill today timesheet', action='store_true', default=False)

args = parser.parse_args()

if __name__ == '__main__':

    if args.today:
        browser = Browser("", "", today_flag=True)

    else:
        browser = Browser(args.start_date, args.end_date)
    
    browser.setup()
    browser.login()

    for day in browser.days_list:
        browser.fill_missing_days(day)
        print(f"Day {day} filled successfully")

    time.sleep(1)
    browser.close()
