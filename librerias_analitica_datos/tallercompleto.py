# -*- coding: utf-8 -*-
"""tallercompleto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17KbVa8qzBpbknLLn8rKp2W82cG8EeBcw

#Importar las librerias
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#usaremos todas las librerias y aquí conoceremos a seaborn, aplicaremos lo aprendido 

pd.options.display.max_columns= None#mostramos el total de mis columnas sin nombres resumidos

"""para importar archivos

"""

Link='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-25-2020.csv'
#Para le.read_csv(Link)erlo

datos=pd
print(datos)
print(datos.info())
print(datos.head())

"""Limpieza de mi df"""

datos.drop(['FIPS','Admin2','Last_Update','Combined_Key','Province_State'],axis=1, inplace=True)
print(datos.head())

"""Agrupar"""

df=datos.groupby('Country_Region')['Confirmed','Deaths','Recovered','Active'].sum().reset_index()

print(df.head(10))
print(df.info())

"""Vamos a ver los primeros 40 paises con mas registros de contagiados"""

primeros=df.sort_values(by=['Confirmed'], ascending=False ).head(40)
print(primeros)

#Vamos a graficar Matplotlib
primeros['Confirmed'].plot(kind='bar')
plt.title('Paises')
plt.show()

#Cpon seaborn
#plt.figure()
plot=sns.barplot(primeros['Confirmed'], primeros['Country_Region'])
for i,(value,name) in enumerate(zip(primeros['Confirmed'],['Country_Region'])):
  plot.text(value, i-0.05, f'{value:,.0f}', size=10)
  plt.show()

#barplot seaborn

plt.figure(figsize=(6,6))
confirmed=sns.barplot(primeros['Confirmed'], primeros['Country_Region'], color='Red', label='Confirmed')
recovered=sns.barplot(primeros['Recovered'], primeros['Country_Region'], color='Green', label='Recovered')

#Grafico de dispersionp

sns.lmplot(x='Confirmed', y='Recovered', data=primeros)

sns.lmplot(x='Confirmed', y='Recovered', data=primeros,
           
           fit_reg=False, #linea de regresion

           hue='Country_Region')

"""Datos del titanic

titanic=sns.load_dataset('titanic')
"""

#Datos del titanic
pd.options.display.max_columns= None

titanic=sns.load_dataset('titanic')
print(titanic.head())

print(titanic.info())

titanic=titanic.dropna()
print(titanic.info())

"""Podemos ver la distribucion de los datos haciendo uso de la funcion distplot()."""

densidad=sns.distplot(titanic['age'])
print(densidad)

print(titanic)

densidad=sns.distplot(titanic['fare'])

#funcion pairplot
sns.pairplot(titanic)

sns.pairplot(titanic,hue='sex')

sns.barplot(x='sex',y='age',data=titanic)

#cuartiles

sns.boxplot(x='sex',y='age',data=titanic)