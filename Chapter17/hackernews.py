import requests 
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("status code:",r.status_code)
ids = r.json()
##gathering the ids from the api 
# Inserting the ids into the link 
name,submission_dict = [],[]
for id in ids[:30]:
    url = ("https://hacker-news.firebaseio.com/v0/item/"+str(id)+'.json' )
    r = requests.get(url)
    detail = r.json()

    sub_dict ={
        'label':detail['title'],
        'xlink':'https://news.ycombinator.com/item?id='+str(id),
        'value':detail.get('descendants',0)
            }
    name.append(detail['title'])
    submission_dict.append(sub_dict)
submission_dict = sorted(submission_dict,key=itemgetter('value'),reverse=True)



my_style = LS('#333366', base_style=LCS)
chart =pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Hacker news comments for topics'
chart.x_labels = name
chart.add('comments',submission_dict)
chart.render_to_file('submisson.svg')

