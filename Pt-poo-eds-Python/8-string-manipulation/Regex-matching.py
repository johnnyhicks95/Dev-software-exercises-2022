from ast import pattern
import sys
import re

# compares to *strings* if they match, inpurt console command
# python regex_generic.py "<pattern>" "<string>"
pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match( pattern, search_string )

if match:
    template = "'{}' matches pattern '{}' "
else:    
    template = "'{}' does not matches pattern '{}' "

print(template.format(search_string, pattern) )
""" 
output-----
python Regex-matching.py "hello worl" "hello world"
'hello world' matches 'hello world 
"""




