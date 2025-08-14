import pandas as pd

city = ['texus', 'clafornia', 'hollywood']

city1 = ['europe', 'astraliya', 'north koria']

city2 = ['bangladesh', 'singapur', 'london']

df = pd.DataFrame(city1)

print(df)
df6 = pd.DataFrame(zip(city, city1, city2), columns=['city_in_usa', 'city_in_europe', 'city_in_asia'], index=['ci', 'c2', 'c3'])

print(df6)








