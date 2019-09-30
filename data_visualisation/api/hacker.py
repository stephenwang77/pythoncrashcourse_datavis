import requests
import pygal
from operator import itemgetter


# API to get JSON of top stories in hacker-news:

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
response = r.json()
top_stories = []
title_list = []

# https://hacker-news.firebaseio.com/v0/item/$[item_name].json
# This returns information about the article

for story_id in response[:10]:
    story_url = 'https://hacker-news.firebaseio.com/v0/item/' + str(story_id) + '.json'
    story_r = requests.get(story_url)
    story_response = story_r.json()
    story_dict = {
        'label' : story_response['title'],
        'xlink' : 'http://news.ycombinator.com/item?id=' + str(story_response['id']),
        'value' : story_response.get('descendants', 0)
    }
    top_stories.append(story_dict)

top_stories = sorted(top_stories, key=itemgetter('value'), reverse=True)
for dict in top_stories:
    title_list.append(dict['label'])

# Check your top stories
"""
for dict in top_stories:
    print('\nTitle: ', dict['title'])
    print(dict['link'])
    print(dict['comments'])
"""

# Config for bar chart

config = pygal.Config()
config.x_label_rotation = 45
config.title_font_size = 24
config.label_font_size = 12
config.truncate_label = 15
config.major_label_font_size = 14
config.width = 1000
config.show_y_guides = False
config.show_legend = False

# Adding values to bar chart

bar_chart = pygal.HorizontalBar()
bar_chart.title = 'Most Discussed Stories'
#bar_chart.add('what the fuck', top_stories)
for x in range(len(top_stories)):
    bar_chart.add(title_list[x], [top_stories[x]])
bar_chart.render_to_file('trial.svg')

# bar_chart.add(string, list/numeric)



"""
https://hacker-news.firebaseio.com/v0/item/$[item_name].json
This returns information about the article:
Comment = descendants
URL = submission_id
Title = title
"""
