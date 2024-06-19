import pandas as pd 
import matplotlib.pyplot as plt

# Leer el archivo CSV
csv = pd.read_csv('fallecidos_covid.csv', sep=';')

# Crear un DataFrame con las columnas seleccionadas usando una lista en lugar de un conjunto
dataframe = pd.DataFrame(csv[['FECHA_FALLECIMIENTO', 'SEXO', 'DEPARTAMENTO']])

# Contar los valores en la columna "SEXO"
sexo = dataframe['SEXO'].value_counts()

# Contar los valores en la columna "DEPARTAMENTO" y seleccionar los primeros 5
departamento = dataframe['DEPARTAMENTO'].value_counts().head()

# Imprimir los valores de "DEPARTAMENTO"
print(departamento)

# Grafica 1
plt.subplot(1, 2, 1)
sexo.plot(kind='pie', autopct='%1.01f%%')
plt.title('SEXO')

# Grafica 2
plt.subplot(1, 2, 2)
departamento.plot(kind='bar', rot=20)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.title('DEPARTAMENTO')

# Título principal
plt.suptitle('GRAFICA COVID 19 - FALLECIDOS')

# Mostrar las gráficas
plt.show()
