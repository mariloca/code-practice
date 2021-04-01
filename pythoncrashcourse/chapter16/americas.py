import pygal.maps.world

wm=pygal.maps.world.World() #make an instance of the World class and set the map's title attribute
wm.title='North, Central, and South America'

#add() method takes a label and a list of codes, each call to add() sets up a new color for the set of countries and adds that color to a key on the left of the graph
wm.add('North America', ['ca','mx','us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])
    
wm.render_to_file('americas.svg')#creates a .svg file, can open in browser