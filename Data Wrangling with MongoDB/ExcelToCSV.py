# -*- coding: utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "data/2013_ERCOT_Hourly_Load_Data.xls"
outfile = "data/2013_Max_Loads.csv"


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    data = {}
    for x in range(1,9):
        station = sheet.cell_value(0,x)

        cv = sheet.col_values(x,start_rowx=1,end_rowx=None)
        
        print len(cv)

        maxValue = max(cv)
        print "MaxValue : {0}".format(maxValue)

        maxPositon = cv.index(maxValue) + 1
        print "Position : {0}".format(maxPositon)

        maxTime = sheet.cell_value(maxPositon,0)
        print "MaxTime : {0}".format(maxTime)

        realTime = xlrd.xldate_as_tuple(maxTime,0)
        print "Real Time : {0}".format(realTime)

        data[station] = {"maxval":maxValue,"maxtime":realTime}

        print "DATA: " + str(data)

    return data


def save_file(data, filename):
    # YOUR CODE HERE
    with open(filename,'w') as file:
        write = csv.writer(file, delimiter='|')
        # Write the HEAD row
        write.writerow(["Station","Year","Month","Day","Hour","Max Load"])
        # write the values in the rows
        for x in data:
            # print data[x]["maxtime"]
            year, month,day,hour,minute,seconds = data[x]["maxtime"]
            write.writerow([x,year,month,day,hour,data[x]["maxval"]])
    pass


def test():
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # # Output should be 8 lines not including header
        # assert number_of_rows == 8

        # # Check Station Names
        # assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()
