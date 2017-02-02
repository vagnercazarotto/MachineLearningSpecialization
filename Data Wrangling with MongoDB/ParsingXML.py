import xml.etree.ElementTree as ET 
import pprint 

tree = ET.parse('data/exampleResearchArticle.xml')
root = tree.getroot()

print "Children of root"
for child in root:
	# print child.tag
	pass

title =  root.find('./fm/bibl/title')
title_text = ""
for p in title:
	# print p.text
	title_text = p.text

print "\nTitle:\n",title_text


print "\nAuthor email adresses:"
for adresses in root.findall('./fm/bibl/aug/au'):
	email = adresses.find('email')
	if email is not None:
		print email.text