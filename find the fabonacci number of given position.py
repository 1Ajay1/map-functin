def fabo(m,fab1=0,fab2=1,sum=0):
             for i in range(m):
                          sum=fab1+fab2
                          fab2=fab1
                          fab1=sum
             return fab1
var=list(map(fabo,[1,2,4,6,3,5,0]))
print(var)
