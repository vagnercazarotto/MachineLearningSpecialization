# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import csv
import pprint

DATADIR = "/Users/vagnercazarotto/Documents/machineLearning/MachineLearningSpecialization/Data Wrangling with MongoDB/data"
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "rU") as f:
        header = f.readline().split(",")
        # first read the head of the file and split, so we can get values to
        # use as Keys
        print header
        counter = 0
        for line in f:
            #print line
            if counter == 10:
                break

            fields = line.split(",")
            entry = {}

            for i, value in enumerate(fields):
                # Enumerate give us a index value, so we
                # can access the apropriate field in head to use as a KEY in
                # our dic
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1

    return data


## ok Now parse data with CSV module

#In a Python with universal newline support open() the mode parameter can also be "U", 
# meaning "open for input as a text file with universal newline interpretation". 
# Mode "rU" is also allowed, for symmetry with "rb"
def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile,'rU') as csvReader:
        reader = csv.DictReader(csvReader)
        for line in reader:
            data.append(line)
    return data



def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_csv(datafile)
    # d = parse_file(datafile)
    print d
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()
