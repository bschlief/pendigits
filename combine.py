import json
import itertools
inputs = open('pendigits_sta16_test.csv','r')
targets = open('pendigits_label_test.csv', 'r')

output_list = []

for inpt, target in itertools.izip(inputs, targets):
    output_list.append( { 'input': [int(x) for x in inpt.split(',')],
                     'target': int(target) } )

print json.dumps(output_list, indent=4)
