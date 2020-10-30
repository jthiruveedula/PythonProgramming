#it is kind of OR condition for finding patters

pattern='am|in|the'
import re
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
# Search Method:  <re.Match object; span=(2, 4), match='am'>
# FindAll Method: ['am', 'am', 'in', 'in', 'in', 'the', 'am', 'in', 'in']