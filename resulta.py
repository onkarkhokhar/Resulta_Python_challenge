import requests
import json


def getdetails(startdate,enddate):
    page_response = requests.get("https://delivery.chalk247.com/scoreboard/NFL/{}/{}.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0".format(startdate,enddate))
    page_content = json.loads(page_response.content.decode('utf-8'))

    page_response2 = requests.get("https://delivery.chalk247.com/team_rankings/NFL.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0")
    page_content2 = json.loads(page_response2.content.decode('utf-8'))

    return page_content,page_content2

startdate=input("Please enter start date in YYYY-MM-DD format:")
enddate=input("Please enter end date in YYYY-MM-DD format:")
# startdate = "2020-01-12"
# enddate = "2020-01-19"

scoreboard, team_ranking = getdetails(startdate,enddate)
final_result = []
for k1,v1 in scoreboard['results'].items():
	if(v1 != []):
		for k2,v2 in scoreboard['results'][k1]['data'].items():
			item = {}
			item['event_id'] = v2['event_id']
			dd = v2['event_date'].split(' ')[0].split('-')[2]
			mm = v2['event_date'].split(' ')[0].split('-')[1]
			yy = v2['event_date'].split(' ')[0].split('-')[0]
			tt = v2['event_date'].split(' ')[1]
			item['event_date'] = dd+'-'+mm+'-'+yy
			item['event_time'] = tt
			item['away_team_id'] = v2['away_team_id']
			item['away_nick_name'] = v2['away_nick_name']
			item['away_city'] = v2['away_city']
			item['home_team_id'] = v2['home_team_id']
			item['home_nick_name'] = v2['home_nick_name']
			item['home_city'] = v2['home_city']
			for value in team_ranking['results']['data']:
				if(value['team_id'] == v2['away_team_id']):
					item['away_rank'] = value['rank']
					item['away_rank_points'] = "{:.2f}".format(float(value['adjusted_points']))
				elif(value['team_id'] == v2['home_team_id']):
					item['home_rank'] = value['rank']
					item['home_rank_points'] = "{:.2f}".format(float(value['adjusted_points']))
			final_result.append(item)
print(final_result)