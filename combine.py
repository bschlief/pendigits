import json
import itertools
import argparse

parser = argparse.ArgumentParser(description="Combine inputs with targets into a list of json objects with a 'input' and 'target' field each.")
parser.add_argument('-r',
    '--representation',
    choices=['dyn', 'sta4', 'sta8', 'sta16'],
    help='dyn=(x,y) representation, staX=X by X bitmap',
    required=True)
parser.add_argument('-t', '--type', choices=['train', 'test'], help='combine either training or test data', required=True)
args = vars(parser.parse_args())

inputs_filename = "pendigits_{0}_{1}.csv".format(args['representation'], args['type'])
targets_filename = "pendigits_label_{0}.csv".format(args['type'])

inputs = open(inputs_filename,'r')
targets = open(targets_filename, 'r')

output_list = []

for inpt, target in itertools.izip(inputs, targets):
    output_list.append( { 'input': [int(x) for x in inpt.split(',')],
                     'target': int(target) } )

print json.dumps(output_list, indent = 2, separators=(',', ': '))
