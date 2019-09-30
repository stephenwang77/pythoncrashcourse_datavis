import requests
import pygal

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
item_dick = response_dict['items']

"""
print(response_dict.keys()) returns
dict_keys(['total_count', 'incomplete_results', 'items'])
"""

"""
for item_dict in item_dick:
    try:
        print('\nName: ' + item_dict['name'])
        print('Owner: ' + item_dict['owner']['login'])
        print('Stars: ' + str(item_dict['stargazers_count']))
        print('Respository: ' + item_dict['html_url'])
        print('Description: ' + item_dict['description'])
    except TypeError:
        pass
"""

# List of dictionaries to plot data with value, label, and xlink

git_name, plot_dicts = [], []
for item_dict in item_dick:
    if item_dict['stargazers_count'] != None and item_dict['description'] != None and item_dict['html_url'] != None:
        git_name.append(item_dict['name'])
        plot_dict = {
            'value' : item_dict['stargazers_count'],
            'label' : item_dict['description'],
            'xlink' : item_dict['html_url']
        }
        plot_dicts.append(plot_dict)


# Configure the bar chart

configuration = pygal.Config()
configuration.x_label_rotation = 45
configuration.show_legend = False
configuration.title_font_size = 24
configuration.label_font_size = 12
configuration.major_label_font_size = 16
configuration.truncate_label = 15
configuration.show_y_guides = False
configuration.width = 1000

# Making the bar chart and adding values

bar_chart = pygal.Bar(configuration)
bar_chart.title = 'Most Starred Python Projects on GitHub'
bar_chart.x_labels = git_name
bar_chart.add('', plot_dicts)
bar_chart.render_to_file('gitstars.svg')
