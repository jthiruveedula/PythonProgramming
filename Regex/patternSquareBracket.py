#Square Brackets pattern will search each element present inside square brackets
#for Eg:- if we want to find special chars from string in tha case we have to give [;'@#%&*(){}] all chars inside square brackets
#wwe can use non method for excluding pattern inside brackets using caret(^) [^0-9] like this


import re

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
pattern='[;,!\']'
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
