def func(min,max,div):
    if(div<1):
        div=1
    for i in range(min,max) :
        if(i % div == 0):
            print(i)
n1=input('Enter minimum')
n2=input('Enter maximum')
n3=input('Enter divisor')
func(int(n1),int(n2),int(n3))
