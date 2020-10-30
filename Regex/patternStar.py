#asterisk is used to find patterns based on left or right position from asterisk


pattern='swi*g'
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
# Search Method:  <re.Match object; span=(17, 22), match='swing'>
# FindAll Method: ['swing']