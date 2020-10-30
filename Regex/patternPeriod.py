#period could be used to find pattern if we are not sure about full word
#in this case we can use place period in middle of that,we can see in below eg

import re
pattern='sw..ging'
string = '''
I am black!
I am swinging in the sky,
I am wringing worlds awry;
I am the thought of the throbbing mills,
I am the soul of the soul-toil kills,
Wraith of the ripple of trading rills;
Up I’m curling from the sod,
I am whirling home to God;
'''

match =re.match(pattern,string)
search =re.search(pattern,string)
findall =re.findall(pattern,string)
split =re.split(pattern,string)
sub =re.sub(pattern,'Ash',string)
print("Match Method: " ,match)
print("Search Method: ",search)
print("FindAll Method:",findall)
print("Split Method: ",split)
print("sub Method: ",sub)