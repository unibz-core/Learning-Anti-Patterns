#nel alloy dot bisogna:
#-> nominare le relazioni, part, mediates, ecc
#-> far vedere i top types object, relator, ecc
#fare due livelli inclusi top tyepes (0, 1) 
#enumerare i livelli (tipo 0, 1, ecc vedi esempio testnew)

import pandas as pd
import networkx as nx
from collections.abc import Mapping
import matplotlib.pyplot as plt
import re
from collections import defaultdict

#here the input must be a .dot->.txt file
a_file = open("car-binover-proc.txt", "r")
clean = [re.sub(r' ', '', i) for i in a_file]
list_of_lists = []
for line in clean:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)
a_file.close()
r = re.compile('N')
filter = [j for i in list_of_lists for j in i if r.findall(j)]
list0 = [''.join(x) for x in filter]
filter1 = [re.sub(r'\,color(.*?)\,label', '', i) for i in list0]
filter2 = [re.sub(r'uuid=', '', i) for i in filter1]
filter3 = [re.sub(r'"\,dir(.*?)\]', '<', i) for i in filter2]
filter4 = [re.sub(r'\,color(.*?)\]', '', i) for i in filter3]
filter5 = [re.sub(r'\,label', '', i) for i in filter4]
filter6 = [re.sub(r'\[(.*?)=', '=', i) for i in filter5]
filter7 = [re.sub(r'=(.*?)\(', '="(', i) for i in filter6]
joined1 = [re.sub(r',', ' ', i) for i in filter7]
joined2 = [re.sub(r'"', '', i) for i in joined1]
joined3 = [re.sub(r'=', ' ', i) for i in joined2]
joined4 = [re.sub(r'this/', '<', i) for i in joined3]
joined5 = [re.sub(r'\(', '', i) for i in joined4]
joined6 = [re.sub(r'\)', '', i) for i in joined5]
list10 = []
for line in joined6:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list10.append(line_list)
list11 = [i[0]+":"+j for i in list10 for j in i]
p = re.compile('<')
list12 = [a for a in list11 if p.findall(a)]
list13 = [re.sub(r'<', '', i) for i in list12]
list14 = [list13[i] for i in range(len(list13))]

#MANAGING RELATIONS
h = re.compile('->') #re.compile('relationtype') - here may need to annotate the type on visual simulator
list15 = [a for a in list14 if h.findall(a)] #generalize relations!!!!!!

hm = re.compile('mediates') #mediates OUTPUT!!!!
list16 = [a for a in list15 if hm.findall(a)]
mediates = []
if len(list16) > 0: 		
	list17 = sorted(list16)
	list18 = [elm + "\"" + "mediates" + str(index) for index, elm in enumerate(list17)]
	mediates = [re.sub(r':(.*?)\"', ':', i) for i in list18] 	
elif len(list16) == 0:
	list16 = False

hp = re.compile('isProperPart') #ppart OUTPUT!!!!
list19 = [a for a in list15 if hp.findall(a)]
ppart = []
if len(list19) > 0: 		
	list20 = sorted(list19)
	list21 = [elm + "\"" + "isProperPart" + str(index) for index, elm in enumerate(list20)]
	ppart = [re.sub(r':(.*?)\"', ':', i) for i in list21] 	
elif len(list19) == 0:
	list19 = False
	
mat = re.compile('material') #material OUTPUT!!!!
list22 = [a for a in list15 if mat.findall(a)]
material = []
if len(list22) > 0: 		
	list23 = sorted(list22)
	list24 = [elm + "\"" + "material" + str(index) for index, elm in enumerate(list23)]
	material = [re.sub(r':(.*?)\"', ':', i) for i in list24] 	
elif len(list22) == 0:
	list19 = False
								
#HERE WE MAY ADOPT re.compile('relationtype') TO FILTER TYPES OF RELATION, E.G. ALL MEDIATES OR ALL PARTS...
#list16 = sorted(list15) #REPEAT FOR EACH RELATION
#list17 = [elm + "\"" + "mediates" + str(index) for index, elm in enumerate(list16)]
#list18 = [re.sub(r':(.*?)\"', ':', i) for i in list17] #RELATIONS OUTPUT!!!!!

#MANAGING RELATORS
rel0 = [' '.join(x) for x in list10]
rel1= [re.sub(r'<Relator', '<0AA', i) for i in rel0]
l = re.compile('<0AA')
rel2 = [a for a in rel1 if l.findall(a)]

#HERE "IF" STATEMENT
rel18 = []
if len(rel2) > 0: 
	rel3 = [i.split() for i in rel2]
	rel4 = [i[0]+":"+j for i in rel3 for j in i]
	rel5 = [a for a in rel4 if p.findall(a)]
	rel6 = sorted(rel5)
	rel7= [re.sub(r'<', '', i) for i in rel6]
	rel8 = [re.sub(r':', ' ', i) for i in rel7]
	rel9 = [i.split() for i in rel8]
	reldict = defaultdict(list)
	for el in rel9: reldict[el[1]].append(el[0])
	reltemp = list(reldict.items())  
	ridx = [idx for idx, key in enumerate(reltemp)]  
	ridxs = ["Relator"+str(item) for item in ridx] #generalize Relator
	rel10 = reldict.items()
	rel11 = [x[1] for x in rel10]
	rel12 = [','.join(sub_list) for sub_list in rel11]
	rel13 = [[i,j] for i,j in zip(ridxs,rel12)] 				#QUI C'è UN ERRORE!!! BISOGNA ORDINARE RIDXS
	rel14 = [i[0]+","+j for i in rel13 for j in i]
	rel15 = [a for a in rel14 if r.findall(a)]
	rel16 = [re.sub(r',', ' ', i) for i in rel15]
	rel17 = [i.split() for i in rel16]
	rel18 = [j+":"+i[0] for i in rel17 for j in i]
elif len(rel2) == 0:
	rel2 = False

rel19 = [a for a in rel18 if r.findall(a)] #RELATORS FIRST OUTPUT!!!!!

#print(ridxs)
#print(rel12)

#MANAGING OBJECTS
ob0 = [' '.join(x) for x in list10]
ob1= [re.sub(r'<Object', '<0AA', i) for i in ob0]
l = re.compile('<0AA')
ob2 = [a for a in ob1 if l.findall(a)]

#HERE "IF" STATEMENT
ob18 = []
if len(ob2) > 0: 
	ob3 = [i.split() for i in ob2]
	ob4 = [i[0]+":"+j for i in ob3 for j in i]
	ob5 = [a for a in ob4 if p.findall(a)]
	ob6 = sorted(ob5)
	ob7= [re.sub(r'<', '', i) for i in ob6]
	ob8 = [re.sub(r':', ' ', i) for i in ob7]
	ob9 = [i.split() for i in ob8]
	obdict = defaultdict(list)
	for el in ob9: obdict[el[1]].append(el[0])
	obtemp = list(obdict.items())  
	oidx = [idx for idx, key in enumerate(obtemp)]  
	oidxs = ["Object"+str(item) for item in oidx] #generalize Object
	ob10 = obdict.items()
	ob11 = [x[1] for x in ob10]
	ob12 = [','.join(sub_list) for sub_list in ob11]
	ob13 = [[i,j] for i,j in zip(oidxs,ob12)]
	ob14 = [i[0]+","+j for i in ob13 for j in i]
	ob15 = [a for a in ob14 if r.findall(a)]
	ob16 = [re.sub(r',', ' ', i) for i in ob15]
	ob17 = [i.split() for i in ob16]
	ob18 = [j+":"+i[0] for i in ob17 for j in i]
elif len(ob2) == 0:
	ob2 = False	
	
ob19 = [a for a in ob18 if r.findall(a)] #OBJECTS FIRST OUTPUT!!!!! 


#print(obtemp)
#print(oidxs)
#print(ob12)

########################################## LEARNING OUTPUT

#joined0 = mediates+ppart
#joined1 = rel19+ob19 
#joined2 = joined0+joined1

#print(rel17)
#print(joined2)
#for i in range(len(joined2)): #ok
 #print(joined2[i])

########################################## object hierarchy not_nested

ob20 = [i for i in ob18 if r.findall(i)]
ob21 = [re.sub(r':', ' ', i) for i in ob20]
ob22 = [i.split() for i in ob21]

ob23 = defaultdict(list)
for k, v in ob22:
    ob23[k].append(v)
ob24 = [] 				
for key, val in ob23.items(): 
    ob24.append([key] + val)
ob25 = [i[1:]+[i[0]] for i in ob24] #REVERSE
ob26 = [item for item in ob25 if len(item) <= 4] #hierarchy till level 3 #graph part 1
#from here sub-hierarchy
ob27 = [item for item in ob25 if len(item) > 4]
ob28 = [[item[0],item[1]] for item in ob27] #link to the root!!! #graph part 2
ob29 = [item[1:] for item in ob27]
prova = ob29 + ob29 #to be removed													#warning!!!!!!!! check if it works!!!
ob30 = [item[1:] for item in ob29] 
ob31 = [[j,i[-1]] for i in ob30 for j in i] # leaves + nodes #graph part 3
ob32 = ob29[:-1]
ob33 = prova
#del ob33[-1][-1] #(remove the last from the last)
#ob34 = [[i[0],j] for i in ob33 for j in i] 		# parents + leaves #graph part 4

ob34 = []
if len(ob33) > 0: 		
	del ob33[-1][-1]
	ob34 = [[i[0],j] for i in ob33 for j in i]
elif len(ob33) == 0:
	ob33 = False

ob35 = ob34 + ob31 + ob28 + ob26
test = ob35

# parents + leaves #graph part 4

#generate hierarchy dictionary
def formTree(test): 
    tree = {} 
    for item in test: 
        currTree = tree  
        for key in item[::-1]:
            if key not in currTree: 
                currTree[key] = {} 
            currTree = currTree[key]              
    return tree 

graph = formTree(test)
print(ob28)

# Empty directed graph
G = nx.DiGraph()

# Iterate through the layers
q = list(graph.items())
while q:
    v, d = q.pop()
    for nv, nd in d.items():
        G.add_edge(v, nv)
        if isinstance(nd, Mapping):
            q.append((nv, nd))

nx.draw(G, with_labels=True)
#plt.show()

#flatten dictionary
#G = nx.Graph(graph)
edges = [e for e in G.edges]
#print(edges)

#GENERATE LABELS FOR .DOT GRAPH NODES #OBJECTS
edges0 = [list(ele) for ele in edges]
edges1 = [','.join(sub_list) for sub_list in edges0]
edges2 = [a for a in edges1 if r.findall(a)]
z = re.compile('^((?!\,N).)*$')
edges3 = [a for a in edges2 if z.findall(a)] 
edges4 = [re.sub(r'\,', ':', i) for i in edges3] 
#print(edges4)

########################################## object nested hierarchy#

obb26 = [','.join(sub_list) for sub_list in ob26]
obb27 = [re.sub(r'\,N', ':N', i) for i in obb26]
obb28 = [i.split(',') for i in obb27] 
obb29 = [[re.sub(r'[A-Z](.*?):', '', j) for j in i] for i in obb28] #hierarchy till level 3 #graph part 1 (collapse Nn) - #ob26collapsed

#obb30 = [[item[0],item[1],item[-1]] for item in ob27] # hierarchy > 4 part 2 (collapse Nn)
obb30 = [[item[1],item[-1]] for item in ob27] # hierarchy > 4 part 2 (collapse Nn)
obb31 = [item[1:] for item in obb30]
prova0 = obb31 + obb31 #to be removed
obb32 = [item[1:] for item in prova0] 
obb33 = [[j,i[-1]] for i in obb32 for j in i] # leaves + nodes #graph part 3
obb34 = obb31[:-1]

obb35 = prova0

obb36 = []
if len(obb35) > 0: 		
	del obb35[-1][-1]
	obb36 = [[i[0],j] for i in obb35 for j in i]
elif len(obb35) == 0:
	obb35 = False

obb37 = obb29 + ob28 + obb30 + obb36
test0 = obb37

def formTree0(test0): 
    tree0 = {} 
    for item in test0: 
        currTree0 = tree0  
        for key in item[::-1]:
            if key not in currTree0: 
                currTree0[key] = {} 
            currTree0 = currTree0[key]              
    return tree0 

graph0 = formTree0(test0)
#print(graph)

# Empty directed graph
GG = nx.DiGraph()

# Iterate through the layers
qq = list(graph0.items())
while qq:
    vv, dd = qq.pop()
    for nvv, ndd in dd.items():
        GG.add_edge(vv, nvv)
        if isinstance(ndd, Mapping):
            qq.append((nvv, ndd))

nx.draw(GG, with_labels=True)
#plt.show()

#flatten dictionary
#GG = nx.Graph(graph)
edgesG = [e for e in GG.edges]
#print(edgesG)

edgesG0 = [list(ele) for ele in edgesG]
edgesG1 = [','.join(sub_list) for sub_list in edgesG0]
#edgesG2 = [a for a in edgesG1 if r.findall(a)]
z = re.compile('^((?!\,N).)*$')
edgesG2 = [a for a in edgesG1 if z.findall(a)] 
edgesG3 = [re.sub(r'\,', '->', i) for i in edgesG2]
edgesG4 = [i + ":is-a" for i in edgesG3]

finoutput = edges4 + edgesG4 + mediates + ppart
#print(finoutput)

########################################## relator hierarchy# not_nested

rel20 = [i for i in rel18 if r.findall(i)]
rel21 = [re.sub(r':', ' ', i) for i in rel20]
rel22 = [i.split() for i in rel21]

rel23 = defaultdict(list)
for k, v in rel22:
    rel23[k].append(v)
rel24 = [] 				
for key, val in rel23.items(): 
    rel24.append([key] + val)
rel25 = [i[1:]+[i[0]] for i in rel24] #REVERSE
rel26 = [item for item in rel25 if len(item) <= 4] #hierarchy till level 3 #graph part 1
#from here sub-hierarchy
rel27 = [item for item in rel25 if len(item) > 4]
rel28 = [[item[0],item[1]] for item in rel27] #link to the root!!! #graph part 2
rel29 = [item[1:] for item in rel27]
provar = rel29 + rel29 #to be removed													#warning!!!!!!!! check if it works!!!
rel30 = [item[1:] for item in rel29] 
rel31 = [[j,i[-1]] for i in rel30 for j in i] # leaves + nodes #graph part 3
rel32 = rel29[:-1]
rel33 = provar

rel34 = []
if len(rel33) > 0: 		
	del rel33[-1][-1]
	rel34 = [[i[0],j] for i in rel33 for j in i]
elif len(rel33) == 0:
	rel33 = False

# parents + leaves #graph part 4

rel35 = rel34 + rel31 + rel28 + rel26
testr = rel35

def formTreer(testr): 
    treer = {} 
    for item in testr: 
        currTreer = treer  
        for key in item[::-1]:
            if key not in currTreer: 
                currTreer[key] = {} 
            currTreer = currTreer[key]              
    return treer 

graphr = formTreer(testr)
#print(graph)

# Empty directed graph
GGr = nx.DiGraph()

# Iterate through the layers
qqr = list(graphr.items())
while qqr:
    vvr, ddr = qqr.pop()
    for nvvr, nddr in ddr.items():
        GGr.add_edge(vvr, nvvr)
        if isinstance(nddr, Mapping):
            qqr.append((nvvr, nddr))

nx.draw(GGr, with_labels=True)
#plt.show()

#flatten dictionary
#GG = nx.Graph(graph)
edgesGr = [e for e in GGr.edges]
#print(edgesGr)


#GENERATE LABELS FOR .DOT GRAPH NODES #OBJECTS
edgesG0r = [list(ele) for ele in edgesGr]
edgesG1r = [','.join(sub_list) for sub_list in edgesG0r]
edgesG2r = [a for a in edgesG1r if r.findall(a)]
z = re.compile('^((?!\,N).)*$')
edgesG3r = [a for a in edgesG2r if z.findall(a)] 
edgesG4r = [re.sub(r'\,', ':', i) for i in edgesG3r] 
#print(edgesG4r)

########################################## relator nested hierarchy

rell26 = [','.join(sub_list) for sub_list in rel26]
rell27 = [re.sub(r'\,N', ':N', i) for i in rell26]
rell28 = [i.split(',') for i in rell27] 
rell29 = [[re.sub(r'[A-Z](.*?):', '', j) for j in i] for i in rell28] #hierarchy till level 3 #graph part 1 (collapse Nn) - #ob26collapsed

#rell30 = [[item[0],item[1],item[-1]] for item in ob27] # hierarchy > 4 part 2 (collapse Nn)
rell30 = [[item[1],item[-1]] for item in rel27] # hierarchy > 4 part 2 (collapse Nn)
rell31 = [item[1:] for item in rell30]
prova0r = rell31 + rell31 #to be removed
rell32 = [item[1:] for item in prova0] 
rell33 = [[j,i[-1]] for i in rell32 for j in i] # leaves + nodes #graph part 3
rell34 = rell31[:-1]

rell35 = prova0r
rell36 = []
if len(rell35) > 0: 		
	del rell35[-1][-1]
	rell36 = [[i[0],j] for i in rell35 for j in i]
	#rel25 = True
elif len(rell35) == 0:
	rell35 = False

rell37 = rell29 + rel28 + rell30 + rell36
test0R = rell37

def formTree0R(test0R): 
    tree0R = {} 
    for item in test0R: 
        currTree0R = tree0R  
        for key in item[::-1]:
            if key not in currTree0R: 
                currTree0R[key] = {} 
            currTree0R = currTree0R[key]              
    return tree0R 

graph0R = formTree0R(test0R)
#print(graph)

# Empty directed graph
GGR = nx.DiGraph()

# Iterate through the layers
qqR = list(graph0R.items())
while qqR:
    vvR, ddR = qqR.pop()
    for nvvR, nddR in ddR.items():
        GGR.add_edge(vvR, nvvR)
        if isinstance(nddR, Mapping):
            qqR.append((nvvR, nddR))

nx.draw(GGR, with_labels=True)
#plt.show()

#flatten dictionary
#GG = nx.Graph(graph)
edgesGR = [e for e in GGR.edges]
#print(edgesG)

#GENERATE LABELS FOR .DOT GRAPH NODES #RELATOR
edgesG0R = [list(ele) for ele in edgesGR]
edgesG1R = [','.join(sub_list) for sub_list in edgesG0R]
#edgesG2 = [a for a in edgesG1 if r.findall(a)]
z = re.compile('^((?!\,N).)*$')
edgesG2R = [a for a in edgesG1R if z.findall(a)] 
edgesG3R = [re.sub(r'\,', '->', i) for i in edgesG2R]
edgesG4R = [i + ":is-a" for i in edgesG3R]
#print(edgesG4R)

#print(edgesG4r)

final = edges4 + edgesG4 + edgesG4r + edgesG4R + mediates + ppart
print(final)

#association0 = [re.sub(r'', 'association0', i) for i in filter5] association mapping 0
#type0 = [re.sub(r'', 'type0', i) for i in filter5] type mapping 0
#j = re.compile('mediates')
#mediates = [a for a in filter7 if j.findall(a)]
#k = re.compile('^((?!mediates).)*$') #does not contain mediates
#types = [a for a in filter7 if k.findall(a)]
#mediates0 = [elm + str(index) + "\"" for index, elm in enumerate(mediates)]
#mediates1 = [re.sub(r'mediates\"', 'mediates', i) for i in mediates0]
#joined = mediates1+types

#ob31 = [re.sub(r'N(.*?)[0-9]', '', i) for i in ob30]

#ob30 = [[i[0],j] for i in ob29 for j in i]

#def deep_reverse(ob26):
     #   """ 
      #  assumes L is a list of lists whose elements are ints
       # Mutates L such that it reverses its elements and also 
       # reverses the order of the int elements in every element of L. 
       # It does not return anything.
      #  """
 #       ob26.reverse()
  #      for sublist in ob26:
   #         sublist.reverse()

#deep_reverse(ob26)









