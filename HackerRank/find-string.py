import re
string = input()[::-1]
sub_string = input()
regex = '(?='+sub_string+')'
print(len(re.findall(regex,string)))
