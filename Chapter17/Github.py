import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url =  requests.get('https://api.github.com/search/repositories?q=language:python&sort=star')
response = url.json()
print("status code : ",url.status_code)
# print(response)
res_dict = response['items']
# print(res_dict)
print("The length of the res:",len(res_dict))
##working with response Dictionary
repo_dicts = res_dict[0]

# print(f"Name: {repo_dicts['name'].title()}")
# print(f"URL : {repo_dicts['url']}")
# print(f"Download : {repo_dicts['downloads_url']}")
# print(f"Stargazers count: {repo_dicts['stargazers_count']}")
name,stargaze = [],[]
##Summarizing the Top Repositories
for rep_dict in res_dict:
    # print(f"Name: {rep_dict['name'].title()}")
    # print(f"URL : {rep_dict['url']}")
    # print(f"Download : {rep_dict['downloads_url']}")
    # print(f"Stargazers count: {rep_dict['stargazers_count']}")
    name.append(rep_dict['name'])
    plot_dic = {'value':rep_dict['stargazers_count'],
                'label':rep_dict['description'],
                'xlink':rep_dict['html_url']
                }
    stargaze.append(plot_dic)
# print(name)
# print(stargaze)
#Visualizing repositories using pygal

chart = pygal.Bar( x_label_rotation=45, show_legend=False)
chart.title = "Most -starred python project on github"
chart.x_labels = name
chart.add('',stargaze)

chart.render_to_file('python_star.svg')
