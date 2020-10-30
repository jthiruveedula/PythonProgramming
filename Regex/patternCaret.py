
#caret is used to search the string from strating position


import re
pattern='^I'
string = '''I am black!
I am swinging in the sky,
I am wringing worlds awry;
'''

match =re.match(pattern,string)
search =re.search(pattern,string)
findall =re.findall(pattern,string)
print("Match Method: " ,match)
print("Search Method: ",search)
print("FindAll Method:",findall)


#output
# Match Method:  <re.Match object; span=(0, 1), match='I'>
# Search Method:  <re.Match object; span=(0, 1), match='I'>
# FindAll Method: ['I']