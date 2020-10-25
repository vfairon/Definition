import requests
from bs4 import BeautifulSoup
fh = open('definition.txt', 'w')
while True: 
	rep = input("What's you word (tape q to quit): ") 	
	if rep == "q":
		break
	URL = 'https://www.larousse.fr/dictionnaires/francais/'
	urll = URL + rep	
	#print (urll)
	page = requests.get(urll)
	soup = BeautifulSoup(page.content, 'html.parser')
	defi = soup.find("li", class_="DivisionDefinition")
	#print (defi.text)
	string = rep + ' : ' + defi.text + " \n"
	fh.write(string)









	urll = ""
	

