#!/usr/bin/env python3


import calendar
import csv
import sys


def makecalendarlist(inputyear):
    inputyear = int(inputyear)
    yearcallist = []
    for month in range(1, 13):
        yearcallist.append(calendar.monthcalendar(inputyear, month))
    return yearcallist

        
def main():
    if len(sys.argv) < 2:
        print('please provide a year as the first argument')
        print('usage - ./' + sys.argv[0] + ' <year>')
        sys.exit(1)


    year = sys.argv[1]
    yearlist = makecalendarlist(year)
    weekheader = calendar.weekheader(3).split(' ')
    weekheader.insert(0, '')
    emptyspace = ['','','','','','','','']

    with open(year + '.csv', 'w') as f:
        csv_writer = csv.writer(f)

        f.write('Calendar for ' + year + '\n')
        f.write('\n')

        monthcounter = 1
        for month in yearlist:
            f.write(calendar.month_name[monthcounter] + '\n')
            for week in month:
                week.insert(0, '')
                csv_writer.writerow(weekheader)
                csv_writer.writerow(week)
                csv_writer.writerow(emptyspace)
                csv_writer.writerow(emptyspace)
            csv_writer.writerow(emptyspace)
            monthcounter += 1


if __name__ == '__main__':
    main()

