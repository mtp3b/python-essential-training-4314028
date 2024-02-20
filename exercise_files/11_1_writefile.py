from argparse import ArgumentParser 

parser = ArgumentParser()

parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program')
parser.add_argument('--text', '-t', required=True, help='The text to write to the file')


arguments = parser.parse_args()

with open(arguments.output, 'w') as f:
    f.write(arguments.text+'\n')

print(f'Wrote "{arguments.text}" to file "{arguments.output}"')