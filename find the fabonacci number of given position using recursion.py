def fabo(m,fab1=0,fab2=1,sum=0):
             if m<=0:
                          return fab1
             else:
                          sum=fab1+fab2
                          fab2=fab1
                          fab1=sum
             return fabo(m-1,fab1,fab2,sum)
var=list(map(fabo,[1,2,4,6,3,5,0]))
print(var)
