import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student.csv')

print(df)
name = df['first_name'].head(8)
gpa = df['hs_gpa'].head(8)
 
# Figure Size
fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(name[0:10], gpa[0:10])
 
# Show Plot
plt.show()