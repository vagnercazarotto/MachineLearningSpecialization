#!/usr/bin/python 
import xlrd


dataFile = "data/2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
	workbook = xlrd.open_workbook(datafile)
	sheet = workbook.sheet_by_index(0)

	data = [[sheet.cell_value(r,col) 
				for col in range(sheet.ncols)]
					for r in range(sheet.nrows)]

	print data[0][0]

	print "\n Cells in a nested loop:"
	for row in range(sheet.nrows):
		for col in range(sheet.ncols):
			if row == 50:
				print sheet.cell_value(row,col)


	print sheet.nrows
	print sheet.cell_type(3,5)
	print sheet.cell_value(3,5)
	print sheet.col_values(3,start_rowx=1,end_rowx=7)
	print sheet.cell_type(1, 0)
	exceltime = sheet.cell_value(1, 0)
	print exceltime
	print xlrd.xldate_as_tuple(exceltime,0)




parse_file(dataFile)