import xml.etree.ElementTree as ET 
import pprint 

tree = ET.parse('data/exampleResearchArticle.xml')
article_file = "data/exampleResearchArticle.xml"
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

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def get_authors(root):
	authors = []
	for author in root.findall('./fm/bibl/aug/au'):
		# create a empty container
		data = {
				"fnm": None,
				"snm": None,
				"email": None
		}
		# find the data and save in the container
		data["fnm"] = author.find('./fnm').text
		data["snm"] = author.find('./snm').text
		data["email"] = author.find('./email').text
		
		authors.append(data)
		# print authors[0]['fnm'].text
	return authors




def test():
    solution = [{'fnm': 'Omer', 'snm': 'Mei-Dan', 'email': 'omer@extremegate.com'}, {'fnm': 'Mike', 'snm': 'Carmont', 'email': 'mcarmont@hotmail.com'}, {'fnm': 'Lior', 'snm': 'Laver', 'email': 'laver17@gmail.com'}, {'fnm': 'Meir', 'snm': 'Nyska', 'email': 'nyska@internet-zahav.net'}, {'fnm': 'Hagay', 'snm': 'Kammar', 'email': 'kammarh@gmail.com'}, {'fnm': 'Gideon', 'snm': 'Mann', 'email': 'gideon.mann.md@gmail.com'}, {'fnm': 'Barnaby', 'snm': 'Clarck', 'email': 'barns.nz@gmail.com'}, {'fnm': 'Eugene', 'snm': 'Kots', 'email': 'eukots@gmail.com'}]
    
    root = get_root(article_file)
    data = get_authors(root)

    assert data[0] == solution[0]
    assert data[1]["fnm"] == solution[1]["fnm"]


test()