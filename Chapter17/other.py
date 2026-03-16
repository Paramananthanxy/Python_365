import requests 
import pygal

#getting the url 
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
r = requests.get(url)
response = r.json()
repo_dict = response['items']
name,star = [],[]
for rep_di in repo_dict:
	name.append(rep_di['name'])
	re_di = {'value':rep_di['stargazers_count'],
		  'xlink':rep_di['html_url'],
		  'label':rep_di['description']
    }

	star.append(re_di)
# print(star)



chart = pygal.Bar()
chart.title = 'Most-starred javascirpt project in Github'
chart.x_labels = name
chart.add('star',star)
chart.render_to_file('chart.svg')