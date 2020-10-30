#Dollar can be used to search item which is ending with desired pattern


import re
pattern=';$'
string = '''I am black!
I am swinging in the sky,
I am wringing worlds awry;'''

match =re.match(pattern,string)
search =re.search(pattern,string)
findall =re.findall(pattern,string)
print("Match Method: " ,match)
print("Search Method: ",search)
print("FindAll Method:",findall)

#output
# Match Method:  None
# Search Method:  <re.Match object; span=(63, 64), match=';'>
# FindAll Method: [';']