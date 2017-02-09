#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'data/patent.data'


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

# build a generator for outfiles


def outfileGenerator(filename):
    n = -1
    while True:
        n += 1
        yield open('{0}-{1}'.format(filename, n), 'w')


def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.

    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """

    # ok, the patter we are loking for is
    pattern = '<?xml'

    # a Iterator for file Names
    OutFileIterator = outfileGenerator(filename)

    with open(filename) as infile:
        for line in infile:

            # NOW CREATE A NEW FILE
            if pattern in line:
                outfile = next(OutFileIterator)

            # write the line
            outfile.write(line)

    pass


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()
