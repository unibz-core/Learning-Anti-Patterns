import re
import pandas as pd
from collections import defaultdict

input = ['N0:Object2', 'N0:Object3', 'N0:Object4', 'N0->Object1:is-a', 'Object1->Object0:is-a']

filter0 = [re.sub(r'N', '"N', i) for i in input]
filter00 = [re.sub(r'O', '"O', i) for i in filter0]
filter000 = [re.sub(r'R', '"R', i) for i in filter00]
filter1 = [re.sub(r'->', '" -> ', i, count=1) for i in filter000]
filter2 = [re.sub(r':', '" [label="', i, count=1) for i in filter1]
filter2x = [re.sub(r'\""', '"', i, count=1) for i in filter2]

#EDGES
j = re.compile('->') #contains
filter3 = [i for i in filter2x if j.findall(i)]
filter4 = [i + "\", style=\"solid\", " + "dir=\"forward\"" + ", weight = \"1\"]" for i in filter3]
filter44 = sorted(filter4,reverse=True)

m = re.compile('is-a') #contains
filter45 = [i for i in filter44 if m.findall(i)]
filter46 = [re.sub(r'style', 'color = "#1a4de4", style', i, count=1) for i in filter45]
km = re.compile('^((?!is-a).)*$') #does not contain
filter47 = [i for i in filter44 if km.findall(i)]
filter48 = filter46 + filter47


#NODES
k = re.compile('^((?!->).)*$') #does not contain
filter5 = [i for i in filter2x if k.findall(i)]
filter6 = [re.sub(r'\" \[label=\"', '" ', i, count=1) for i in filter5]
filter7 = [i.split() for i in filter6]
reldict = defaultdict(list)
for el in filter7: reldict[el[0]].append(el[1])
filter8 = reldict.items()
filter9 = [x[0] for x in filter8]
filter10 = [x[1] for x in filter8]
filter11 = [','.join(sub_list) for sub_list in filter10]
filter12 = [[i,j] for i,j in zip(filter9,filter11)]
filter13 = [i[0]+","+j for i in filter12 for j in i] 
w = re.compile('^((?!\"\,\").)*$') #does not contain
filter14 = [i for i in filter13 if w.findall(i)]

#ADD INSTANCE INFO IN TYPE
filter15 = [[i,j] for i,j in zip(filter9,filter14)]
filter16 = [i[0]+","+j for i in filter15 for j in i]
del filter16[0::2] #CHECK IF IT IS ALWAYS VALID
filter17 = [re.sub(r'\,', ' [label=', i, count=1) for i in filter16]
filter18 = [re.sub(r'\",', '\n', i, count=1) for i in filter17]
#filter18 = [re.sub(r'\,', ', label="', i, count=1) for i in filter17]
filter19 = [i + "\"" + ", shape=\"box\", style=\"filled, solid\"]" for i in filter18]


joined = filter48+filter19
print(joined)

print("digraph" + " " + "\"graph\"" + " " + "{")
print("graph" + " " + "[fontsize=12]")
print("node" + " " + "[fontsize=12]")
print("edge" + " " + "[fontsize=12]")
print("rankdir=TB;")

for i in range(len(joined)): #ok
 print(joined[i])
#print(joined)

print("}")


