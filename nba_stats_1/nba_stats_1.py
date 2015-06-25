import requests
import json

for i in range(0,30): #Iterating for 30 Nba teams
	team_id=1610612737+i
	url = 'http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2014-15&TeamID='+ str(team_id)
	r = requests.get(url)
	data= json.loads(r.text)
	
	if(i==0):    #To print all headers once
		for element in data['resultSets'][0]['headers']:
			print element,
			print ",",
		print ""


	for element in data['resultSets'][0]['rowSet']:
		for elements in element:
			elements= str(elements)
			elements = elements.replace(',', '') #To remove any commas within elements. TO ensure that there is no mix up in final csv file.
                  	print elements,
                  	print ",",
		print ""
