# d=[[0 for i  in range(l)] for j in range(l)]  (this line only for understanding)
        x=[[0 for i  in range(l)] for j in range(l)]
        for i in range(l):
          for j in range(i,l):
            st=s[i:j+1]
            # d[i][j]=st  (this line same)
            x[i][j]= (st==st[::-1])    
