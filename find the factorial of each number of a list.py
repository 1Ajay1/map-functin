def fact(var):
             m=1
             for i in range(1,var+1):
                          m*=i
             return m
var=list(map(fact,[2,3,4,1,5,6]))
print(var)
                          
