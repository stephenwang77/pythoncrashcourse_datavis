import requests
import pygal
from pygal.style import LightenStyle

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
r = requests.get(url)
response_dict = r.json()
item_dict_but_is_actually_a_list = response_dict['items']

project_name = []
plot_dicts_but_is_actually_a_list = []

for item in item_dict_but_is_actually_a_list:
    try:
        project_name.append(item['name'])
        information = {
            'value' : item['stargazers_count'],
            'label' : item['description'],
            'xlink' : item['html_url']
        }
        plot_dicts_but_is_actually_a_list.append(information)
    except:
        pass

my_style = LightenStyle('#336676', step=5)


configuration = pygal.Config()
configuration.x_label_rotation = 45
configuration.title_font_size = 24
configuration.label_font_size = 12
configuration.truncate_label = 15
configuration.major_label_font_size = 14
configuration.width = 1000
configuration.show_y_guides = False
configuration.show_legend = False

bar_chart = pygal.HorizontalBar(configuration, style=my_style)
bar_chart.title = 'Most Starred Java Projects on GitHub'
bar_chart.x_labels = project_name
bar_chart.add('', plot_dicts_but_is_actually_a_list)
bar_chart.render_to_file('javagithub.svg')
