import pandas as pd 


#df= pd.read_csv('deliveries.csv')
#print(df.head(100))

data ={ "name": ['vivek','rajni'','devbabu','manisha','ranjit','vinay'],
       "age":[22,24,23,21,20,25],
       "salary":[50000,60000,70000,80000,90000,100000],
       "performance_score":[85,90,78,92,88,95]
       }

df = pd.DataFrame(data)
print(df)
df.salary = df.salary *5
print(df)

print('data modified')
print(df.drop(columns=['performance_score','age'], inplace=True))
print(df)