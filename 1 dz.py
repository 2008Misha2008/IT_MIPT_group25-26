#3.4
l=list(map(int, input().split())) 
for i in range(0, len(l)-1, 2):  l[i], l[i+1] = l[i+1], l[i]
print(l) 

#3.5
l=list(map(int, input().split())) 
print(l[-1:] + l[:-1]) 

#3.6
l=list(map(int, input().split())) 
for i in l:
    if l.count(i) == 1:
        print(i)
        
#3.7
l=list(map(int, input().split())) 
y = l[0]         
k = l.count(y)  
for i in l:
    x = l.count(i)  
    if x > k:   
        y = i             
        k = x 
print(y) 

