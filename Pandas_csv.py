import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('weight-height.csv', delimiter=";")

print (df)
print(type(df))

df.Height *=2.54
df.Weight /=2.2

print(df.head(3)) #pierwsze trzy wiersze

print('\nWykres')
plt.hist(df.Weight, 50)
plt.show()


#print(df.describe())




