"""
Generate the truth table for any expression.
--------------------------
Usage:
1. Install requirements
    $ pip install -r requirements.txt
2. Run truth_table_generator.py and pass the predicate
    $ python truth_table_generator.py 'a,b,c,d' '(a or b) and (c or d)' 'a and b'

NOTE: see `library reference <https://github.com/chicolucio/truth-table-generator#operators-and-their-representations>`_
for details about how to pass expressions
"""
import argparse

from ttg import Truths

parser = argparse.ArgumentParser(description='Draw a truth table')
parser.add_argument('variables', metavar='Variables', type=str, nargs=1, help='variables in the truth table')
parser.add_argument('expressions', metavar='Expression', type=str, nargs='+', help='expression(s) in the truth table')

args = parser.parse_args()

print(Truths(args.variables[0].split(','), args.expressions))
