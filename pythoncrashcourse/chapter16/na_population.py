'''Practice plotting numerical data on a map'''
import pygal.maps.world as py 

wm=py.World()
wm.title='Populations of Countries in North America'
#pass a dictionary as the second argument
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
#pygal automatically use the numbers to shade the countries from light to dark
wm.render_to_file('na_populations.svg')


