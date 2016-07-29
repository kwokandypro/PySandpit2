#!/bin/python

#for i in range(1,21):
#	varia[i-1] = input("tape ton nombre")
#
#print(varia)

def type_your_int():
    varia = [input("tape ton chiffre \n") for i in range(1,21)]
    varia = [[i,val] for val,i in enumerate(varia)]
    varia = [[int(x),y] for x,y in varia]
    global max_varia
    max_varia = max(varia)
    print("La valeur max est " + str(max_varia[0]) + " et la position est " + str(max_varia[1]))

#generation d'emails aleatoires

#file = open('email.txt','w')

import random,string,sys

with open("email.txt","w") as filename:
    for i in range(20):
        filename.write(''.join(random.sample(string.ascii_lowercase,random.randint(5,10)))+'@gmail.com'+'\n')        

# exo
def gen_big(big_s):
    for i in range(1,101):
        if i % 10 == 0:
            big_s.extend([1,2,3])
        else:
            big_s.append(i)

def looking_patt(big_s,pattern,cursor,found):
    for i in big_s:
        if i == pattern[cursor]:
            print("1st if : pour i :"+str(i)+" pour pattern :"+str(pattern[cursor]))
            cursor += 1
            if cursor == len(pattern):
                found.append(pattern)
                print(found)
                print("2eme if : pour cursor :"+str(cursor)+" pour pattern :"+str(pattern) +" pour len de pattern "+str(len(pattern)))
                cursor = 0
        else:
            cursor = 0  
    
    print(len(found) > 0)

#2nd version

def looking_patt(pattern,cursor,found):
    big_s = []
    for i in range(1,101):
        if i % 10 == 0:
            big_s.extend([1,2,3])
        else:
            big_s.append(i)
    # check control
    print(big_s)

    for i in big_s:
        if i == pattern[cursor]:
            print("1st if : pour i :"+str(i)+" pour pattern :"+str(pattern[cursor]))
            cursor += 1
            if cursor == len(pattern):
                found.append(pattern)
                print(found)
                print("2eme if : pour cursor :"+str(cursor)+" pour pattern :"+str(pattern) +" pour len de pattern "+str(len(pattern)))
                cursor = 0
        else:
            cursor = 0  
    
    print(len(found) > 0)


#import re
#for i in big_s:
#    if re.search('1,2,3' , str(i)): 
#        print("pattern found")
#    else:
#        print("pattern not found")
#
#
#pattern = '1,2,3'
#
#for item in big_s:
#    line = ''
#    for number in item:
#        line += str(number)
#    if pattern in line:
#        print('pattern found: %s' % item)    
#
#def getsubidx(x, y):
#    l1, l2 = len(x), len(y)
#    for i in range(l1):
#        if x[i:i+l2] == y:
#            return i            
#
#def subfinder(mylist, pattern):
#    matches = []
#    for i in range(len(mylist)):
#        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
#            matches.append(pattern)
#    print(len(matches[0]),len(pattern))
#    return matches
#
#    if len(pattern) == len(matches[0]):
#        return True
#    else:
#        return False       

#def subfinder(biglist, searchlist):
#    list(filter(lambda x: x in searchlist, biglist))
#
#        return True
#    else:     
#        return False 


# def subfinder(mylist, pattern):
#    matches = []
#    for i in range(len(mylist)):
#        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
#            matches.append(pattern)
#    return matches  


# funcs = (
#     lambda:ab.extend([1, 2, 3]),
#     lambda:ab.append(i)

# )
# ab = []
# for i in range(10):
#     funcs[i % 2]()
# print(ab)
# #output
# [1, 2, 3, 1, 1, 2, 3, 3, 1, 2, 3, 5, 1, 2, 3, 7, 1, 2, 3, 9]

# @AndyK Exactly. Lambdas are just a convenient way to write simple, throw-away functions. 
# They're pretty limited. They don't have a proper name, 
# and they can't do assignments. They're basically just a way of executing a single expression.


 # ab = [i  if i % 2 == 0 ab.extend([1,2,3]) else ab.append(i) for i in range(10)] #my list comprehension

 # ab = [u for a in [[i] if i % 2 else [1, 2, 3] for i in range(10)] for u in a] #PM2ring list incomprehension

# temp = [([1,2,3],[i])[i%2] for i in range(10)]
# print(temp)
# ab = [u for a in temp for u in a]
# print(ab)
# #output
# [[1, 2, 3], [1], [1, 2, 3], [3], [1, 2, 3], [5], [1, 2, 3], [7], [1, 2, 3], [9]]
# [1, 2, 3, 1, 1, 2, 3, 3, 1, 2, 3, 5, 1, 2, 3, 7, 1, 2, 3, 9]



# import random,string,sys
# 
# orig_stdout = sys.stdout
# f = file('email.txt', 'w')
# sys.stdout = f
# 
# for i in range(20):
#     print(''.join(random.sample(string.ascii_lowercase,random.randint(5,10)))+'@gmail.com')
# 
# sys.stdout = orig_stdout
# f.close()
# 
# Code Test: Given an array of ints, return True if the sequence.. 1, 2, 3, .. appears 
# in the array somewhere.
# input("type your string \n")
# 
#with open("email.txt", "w") as tito:
#    for i in range(20):
#        tito.write("Tito is happy")        

#varia = [(val, i) for val,i in enumerate(varia)]
#varia.sort()
#
#
#from operator import itemgetter
#seq = [1, 3, 4, 6, 2, 5]
#print(max(enumerate(varia), key=itemgetter(1, 0)))
##output
#(3, 6)
#
#  
#
#
#max_pos = 0
#max_value = -1
#for i, value in enumerate(varia):
#    if value > max_value:
#        max_value = value
#        max_pos = i
#varia.sort()
#print(max_value)
#print(max_pos)