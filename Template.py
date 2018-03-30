import json, pprint
filename = "/Users/Willy/WebstormProjects/SoftStepIntegrationScripts/DelBQuadPreset.json"
json_data = open(filename).read()
#print(file.read())

ss_dict = json.loads(json_data)
# for value in ss_dict:
#     print(value)
import re

class Key:
    def __init__(self):
        self.key
        self.key_diplay
        self.key_display_name_default
        self.data_type
        self.data_range

### Deep Parse on distinct items
r = []

for key, value in ss_dict.items():
    # modlines
    if key[3:5] == '10':
        #print(key, value)
        p = re.compile(r'(?P<key>\d+)_(?P<element>\w+)(?P<modlinenum>\d+)_(\w+)')
        #p = re.compile(r'(?P<key>\d+)_(\w+)_(\w+)')
        r.append(p.split(key))
        for a in r:
            if a == '':
                r.remove(a)
        #print(r)
    # key control
    elif key[0:2] == '10':
        #print(key, value)
        p = re.compile(r'(?P<key>\d+)_(key)_(?P<element>\w+)_(?P<modlinenum>\w+)')
        r.append(p.split(key))
        #print(p.split(key))
    elif key[0:3] == 'nav':
        #print(key, value)
        p = re.compile(r'(?P<key>\w+)_(?P<element>\w+)(?P<modlinenum>\d+)_(\w+)')
        # p = re.compile(r'(?P<key>\d+)_(\w+)_(\w+)')
        r.append(p.split(key))
        #r = p.split(key)
        #print(r)
    elif key[0:6] == 'preset':
        #print(key)
        p = re.compile(r'(\w+)_(\w+)')
        r.append(p.split(key))
        #r = p.split(key)
# for a in r:
#     print(a)


### Simple Parse on all results
all_results = []
for key, value in ss_dict.items():
    p = re.compile(r'_')
    r = p.split(key)
    r.append([value][0])
    all_results.append(r)

for x in all_results:
    print(x)

pprint.pprint(ss_dict)
# p = re.compile(r'(.*)_(.*)_(.*)_?(.*)')
# p.split('This is a test_short and sweet_of split().')
# print(p.split('This is a_test_short and_sweet of split().'))