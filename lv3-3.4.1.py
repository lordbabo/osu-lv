import pandas as pd
import numpy as np

data = pd.read_csv('data_C02_emission.csv')


print(len(data))
print(data.dtypes)
print(data.drop_duplicates())
for column in ['Transmission','Fuel Type']:
    data[column] = data[column].astype('category')
print(data.dtypes)

# b)
sortedData = data.sort_values(by=['Fuel Consumption City (L/100km)'], ascending=True)[['Make','Model','Fuel Consumption City (L/100km)']]
sortedDataDesc = data.sort_values(by=['Fuel Consumption City (L/100km)'], ascending=False)[['Make','Model','Fuel Consumption City (L/100km)']]
print(sortedData.head(3))
print(sortedDataDesc.head(3))

# c)
selectedData=data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
length=len(selectedData['Make'])
print(f"Broj vozila s veličinom motora između 2.5 i 3.5 L: {length}")
prosjecnaEmisija = data['CO2 Emissions (g/km)'].mean()
print(f"Prosječna emisija C02 plinova: {prosjecnaEmisija}")

# d)
markaAuta = data[data['Make'] == 'Audi']
autoLen = len(markaAuta['Make'])
print(f"Postoji {autoLen} Audija")

numberOfCylinders = markaAuta[markaAuta['Cylinders'] == 4]
print(f"Prosječna C02 emisija je: {numberOfCylinders['CO2 Emissions (g/km)'].mean().round()}")

# e)
sortedByCylinders=data['Cylinders'].value_counts().sort_index()
print(sortedByCylinders)

emissionPerCylinder=data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
print(emissionPerCylinder)

# g)
dizelAutomobili = data[(data['Fuel Type'] == 'D')]
benzinAutomobili = data[(data['Fuel Type'] == 'Z')]

dizel4cilindra=dizelAutomobili

# h)
rucniMjenjac=data[(data['Transmission'].str[0] == 'M')]
length=len(rucniMjenjac['Make'])
print(f"Postoji {length} auta s ručnim tipom mjenjača")

# i)

print(data.corr(numeric_only=True))
