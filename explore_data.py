import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes_ficticios_abril2025.csv')
print(df.describe())

plt.figure(figsize=(10, 6))
sns.histplot(df['Ingresos_Mensuales'], bins=50)
plt.title('Distribución de Ingresos Mensuales (Argentina, Abril 2025)')
plt.xlabel('Ingresos Mensuales ($ pesos argentinos)')
plt.ylabel('Cantidad de Clientes')
plt.savefig('income_distribution_april2025.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Tipo_Empleo', hue=df['Apto_Prestamo'].map({1: 'Apto', 0: 'No Apto'}), data=df)
plt.title('Aptitud para Préstamos por Tipo de Empleo')
plt.xlabel('Tipo de Empleo')
plt.ylabel('Cantidad de Clientes')
plt.legend(title='Elegibilidad')
plt.savefig('loan_eligibility_by_employment_april2025.png')
plt.show()

# Seleccionar solo columnas numéricas para la correlación
numeric_df = df.select_dtypes(include=['int32', 'int64', 'float64'])
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('correlation_matrix_april2025.png', bbox_inches='tight')
plt.show()