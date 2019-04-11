import pandas as pd
i=[]
v=[]
counter=1
while True:
    print(counter)
    x=input()
    if(x == "f"):
        break
    
    i.append(x)
    x=input()
    v.append(x)
    counter+=1
dict = {'v': v, 'i': i} 
df=pd.DataFrame(dict)
df.to_csv("data.csv",index=False)
