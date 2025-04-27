import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes_ficticios_abril2025.csv')
print(df.describe())

plt.figure(figsize=(10, 6))
sns.histplot(df['Ingresos_Mensuales'], bins=50)
plt.title('Distribución de Ingresos Mensuales (Argentina, Abril 2025)')
plt.xlabel('Ingresos Mensuales ($)')
plt.savefig('income_distribution_april2025.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Tipo_Empleo', hue='Apto_Prestamo', data=df)
plt.title('Aptitud para Préstamos por Tipo de Empleo')
plt.savefig('loan_eligibility_by_employment_april2025.png')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.savefig('correlation_matrix_april2025.png')
plt.show()