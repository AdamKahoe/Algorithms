def sqr(a):
    return a*a*a
        n=int(raw_input())
        if(n==0):
            print "[]"
        elif(n==1):
            print "[0]"
        else:
            ar=[0]*n
            ar[0]=0
            ar[1]=1
            for i in range(2,n):
                ar[i]=ar[i-1]+ar[i-2]

            ar=map(sqr,ar)
            print