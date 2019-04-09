def det(l):
    n=len(l) #se toma el tamaño de la matriz
    if (n>2):
        i=1
        t=0 #iterador de columnas
        sum=0 #valor del determinante
        while t<=n-1: #mientras las columnas sean menor o igual a n
            d={} #declaracion de lista
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1)) #laplace
            i=i*(-1)
            t+=1
        print("det:",sum)
        return sum
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0])

l = [[3,0,-2],[4,8,-2],[-2,-2,4]]
det(l)
