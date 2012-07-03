import re
''''
def isEmail(inp):
    return re.search(r'([\w\.-[^$]]+)@(\w+\.\w+)',inp)!=None
inp=raw_input('pLEASE input your email.......')
print isEmail(inp)


files=raw_input('Please input files')

def getTxt(files):
    return re.findall(r'\w+\.txt',files)


print getTxt(files)

inp=raw_input('please input string for percentage.......')

def percAwesome(inp):
     list_inp=inp.split()
     length_inp=float(len(inp.split()))
     match=re.findall(r'awes[o|0]me' ,inp)
     length_foundp=float(len(match))
     return (length_foundp/length_inp)*100
print percAwesome(inp)

'''

#challenge Problems


