# 7777777777777777          # print(i, j)

# greater then or less then 

a = [3,2,3,3,5,9]
b = [1,4,6,5,8]
sum = 0 

for i in a:
        if len(b) > len(a) :
             a.append(0)
        for j in b:
            if j < i :
                if len(a) > len(b):
                    b.append(0)
            # elif len(b) > len(a):
                 
            
                print(i, j)
