my_dict = {}
my_dict = dict()

my_dict = {
    'key': 'value'
}

my_dict = dict(key="value")

steve = {
    'name': 'steve',
    'weight': 155.5,
    'height': 70,
    'foods': ['country fried steak', 'fried chicken', 'collards'],
    'ice cream': {
        'vanilla': False,
        'chocolate': True,
        'coffee': False,
    },
    10: 'this has an integer key',
}

# name_of_dict[KEY]
#print(steve.get('name', 'no candy list'))
#steve['name'] = 'joe'
#print(steve)
#my_list = [1, 2, 3]
#my_list[1] = 'WOW'
#print(my_list)

steve.update({'candies': ['snickers', 'mars', 'm&ms']})
print(steve)
del steve['candies']
print(steve)

print(steve.values())
for key, value in steve.items():
    if isinstance(value,list):
        print(f"The list is at {key}")