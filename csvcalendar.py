"""
A script to create a calendar of a particular year in the
CSV (comma seperated values) format. This can then be edited in most
spreadsheet applications.

usage - python3 csvcalendar.py

The calendar is output in the current working directory and the filename is
"<year>.csv" e.g. 2021.csv for the year 2021.

written by Thomas W Whittam
"""


import calendar
import csv
import sys


def makecalendarlist(inputyear):
    """
    create a list of dates to build the calendar
    each month is a list and inside that is a list for each week of that month

    Args:
        inputyear(int): the year to make a calendar for

    Returns:
        yearcallist(list): a list (year) of lists (months) of lists (weeks)
    """
    yearcallist = []
    for month in range(1, 13):
        yearcallist.append(calendar.monthcalendar(inputyear, month))
    return yearcallist


def main():
    """
    main program code
    """
    print('CSV calendar creator')
    try:
        year = int(input('please enter a year: '))
    except ValueError:
        print('You need to enter a year!')
        sys.exit(1)
    yearlist = makecalendarlist(year)
    weekheader = calendar.weekheader(3).split(' ')
    weekheader.insert(0, '')
    emptyspace = ['', '', '', '', '', '', '', '']
    with open('{}.csv'.format(year), 'w') as fcal:
        csv_writer = csv.writer(fcal)
        fcal.write('Calendar for {}\n'.format(year))
        fcal.write('\n')
        monthcounter = 1
        for month in yearlist:
            fcal.write(calendar.month_name[monthcounter] + '\n')
            for week in month:
                week.insert(0, '')
                csv_writer.writerow(weekheader)
                csv_writer.writerow(week)
                csv_writer.writerow(emptyspace)
                csv_writer.writerow(emptyspace)
            csv_writer.writerow(emptyspace)
            monthcounter += 1
    print('calendar created for year {}'.format(year))


if __name__ == '__main__':
    main()
