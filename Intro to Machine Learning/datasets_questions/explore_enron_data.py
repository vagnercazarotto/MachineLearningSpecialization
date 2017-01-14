#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
personInIntereet = 0

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
for each in enron_data:
	if enron_data[each]["poi"]==1:
		personInIntereet = personInIntereet + 1

print personInIntereet

print enron_data["PRENTICE JAMES"].keys()

print enron_data['PRENTICE JAMES']['total_stock_value'] 



print [s for s in enron_data.keys() if "WESLEY" in s] # ['COLWELL WESLEY']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi'] # 11

print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']



execs = [s for s in enron_data.keys() if ("SKILLING" in s) or ("LAY" in s) or ("FASTOW" in s)]
print execs
print max([(enron_data[person]['total_payments'],person) for person in execs])

##### How many folks in this dataset have a quantified salary? What about a known email address? 
print len([enron_data[person]['salary'] for person in enron_data if enron_data[person]['salary'] != 'NaN'])
print len([enron_data[person]['email_address'] for person in enron_data if enron_data[person]['email_address'] != 'NaN'])

# How many people in the E+F dataset (as it currently exists) have 'NaN' for their total payments? What percentage of people in the dataset as a whole is this?
print (len([enron_data[person]['total_payments'] for person in enron_data if enron_data[person]['total_payments'] == 'NaN']))
print float(len([enron_data[person]['total_payments'] for person in enron_data if enron_data[person]['total_payments'] == 'NaN'])) / float(len(enron_data.keys())) * 100 



# How many POIs in the E+F dataset have NaN for their total payments? What percentage of POIs as a whole is this?
poi_names_file = open("../final_project/poi_names.txt","r")
poi_names = poi_names_file.readlines()
poi_names_file.close()
poi_names = poi_names[2:]
poi_names = [name.split(" ",1)[1].strip("\n") for name in poi_names]
poi_names2 = [name.split(", ") for name in poi_names]
print len(poi_names)


print len([enron_data[person]['total_payments'] for person in enron_data if (enron_data[person]['poi'])])


