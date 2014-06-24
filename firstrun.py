# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
y = 4*7

#%%
name = raw_input('Enter file:') 
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word 
        bigcount = count 
print bigword, bigcount
#%%

#%%
# import random
for i in range(20):
    x = random.random()
    print x
#%%

#%%
for i in range(10):
    x = random.randint(0, 100)
    print x
#%%
    
#%%
x = np.arange (1, 101)   
#%%

#%%
def getMedian():
    prompt = 'Enter a whole number of elements in a random array: '
    input = raw_input(prompt)
    myArray = np.array()    
        for i in range(input):
            x = random.random()
            myArray = myArray + x
    print 'Mean of array: '
    print np.mean(myArray)
    print 'Median of array: '
    print np.median(myArray)
#%%

#%%
myArray = np.zeros(5)   
for i in range(5):
        x = random.random()
        myArray.append(x)

print myArray
          
#%%

#%%

print "Hello World!"

#%%

