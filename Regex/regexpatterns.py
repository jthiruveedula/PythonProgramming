#Regex is a sequence of characters that define a search pattern
#To specify regular exp, metachars are used. Metacharacters are chars that are interpreted with a special meaning

#(re) moudle could be used for regeluar expressions using find, search, find, split, sub functions

#re.match --> matches the regex pattern in 1st position of string
#re.search --> method returns match object if there is any match found in any position in the string
#re.findall --> returns a list that contains all patterns int the string
#re.split --> return a list in which the string has been spit in each match
#re.sub --> replace of matches in string

#MetaCharacters

#[] --> Square Brackets
#. --> period
#^ --> caret
#$ --> dollar
#* --> asterisk
#+ --> plus
#? --> QuestionMark
#{} --> Braces
#() --> group
#\ --> Backslash
#| --> pipe


import re

string = '''
I am the Smoke King
I am black!
I am swinging in the sky,
I am wringing worlds awry;
I am the thought of the throbbing mills,
I am the soul of the soul-toil kills,
Wraith of the ripple of trading rills;
Up I’m curling from the sod,
I am whirling home to God;
I am the Smoke King
I am black.
'''
pattern='Smoke'
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
