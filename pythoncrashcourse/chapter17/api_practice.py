import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call and store the response.
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status Code:", r.status_code) #code 200 indicates a successful response

#Store API response in a variable
response_dict=r.json() #json() converts information to a dict
print("Total repositories: ", response_dict['total_count'])

#Explore information about the repositories
repo_dicts=response_dict['items']
#print("Repositories returned:", len(repo_dicts))

names,plot_dicts=[],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	#stars.append(repo_dict['stargazers_count'])

	#Get the project description, if one is available
	description=repo_dict['description']
	if not description:
		description="No description provided."
	plot_dict = {'value': repo_dict['stargazers_count'], 'label':description,} #value to determine bar height, label to create tooltip for each bar.
	plot_dicts.append(plot_dict)

#Make visualization
my_style=LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14 #labels on x-axis, most numbers on y axis
my_style.major_label_font_size = 18 #labels on y-axis mark off 50000 increments; 

my_config = pygal.Config() #instance of Config class
my_config.x_label_rotation = 45
my_config.show_legend = False #Only plot one series on the charts so show_legend=F
my_config.truncate_label = 15 #Truncate x label to 15 characters
my_config.show_y_guides = False #hide horizontal lines on the graph
my_config.width = 1000 #custome bar width

chart = pygal.Bar(my_config, style=my_style)
chart.title='Most-starred Python Projects on GitHub'
chart.x_labels=names

chart.add('',plot_dicts) #height of the bar. Don't need to be labeled, so pass an empty string
chart.render_to_file('python_repos.svg')

'''
#Examine the first repositories
repo_dict=repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

print("\nSelected information about first respository:")
for repo_dict in repo_dicts:
	print("\nName:", repo_dict['name'])
	print("Owner:", repo_dict['owner']['login'])
	print("Stars:", repo_dict['stargazers_count'])
	print("Repository:", repo_dict['html_url'])
	print("Description:", repo_dict['description'])

#Process results.
#print(response_dict.keys())
'''