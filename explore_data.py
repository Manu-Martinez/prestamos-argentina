import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes_ficticios_abril2025.csv', encoding='utf-8')
print(df.describe())

# Histograma de Ingresos Mensuales (promedio feb-mar-abr 2025)
plt.figure(figsize=(10, 6))
sns.histplot(df['Ingresos_Mensuales'], bins=50)
plt.title('Distribución de Ingresos Mensuales (Promedio Feb-Abr 2025, Argentina)')
plt.xlabel('Ingresos Mensuales ($ pesos argentinos)')
plt.ylabel('Cantidad de Clientes')
plt.savefig('income_distribution_feb_apr2025.png')
plt.show()

# Paleta de colores personalizada para todos los gráficos
custom_palette = {'Apto': 'tab:blue', 'No Apto': 'tab:orange'}

# Gráfico de elegibilidad para préstamo pequeño
plt.figure(figsize=(10, 6))
sns.countplot(x='Tipo_Empleo', 
              hue=df['Apto_Prestamo_Pequeño'].map({1: 'Apto', 0: 'No Apto'}), 
              data=df,
              palette=custom_palette)
plt.title('Aptitud para Préstamo Pequeño ($30,000-$100,000) por Tipo de Empleo')
plt.xlabel('Tipo de Empleo')
plt.ylabel('Cantidad de Clientes')
plt.legend(title='Elegibilidad')
plt.savefig('loan_eligibility_small_by_employment_april2025.png')
plt.show()

# Gráfico de elegibilidad para préstamo mediano
plt.figure(figsize=(10, 6))
sns.countplot(x='Tipo_Empleo', 
              hue=df['Apto_Prestamo_Mediano'].map({1: 'Apto', 0: 'No Apto'}), 
              data=df,
              palette=custom_palette)
plt.title('Aptitud para Préstamo Mediano ($100,001-$500,000) por Tipo de Empleo')
plt.xlabel('Tipo de Empleo')
plt.ylabel('Cantidad de Clientes')
plt.legend(title='Elegibilidad')
plt.savefig('loan_eligibility_medium_by_employment_april2025.png')
plt.show()

# Gráfico de elegibilidad para préstamo elevado
plt.figure(figsize=(10, 6))
sns.countplot(x='Tipo_Empleo', 
              hue=df['Apto_Prestamo_Elevado'].map({1: 'Apto', 0: 'No Apto'}), 
              data=df,
              palette=custom_palette)
plt.title('Aptitud para Préstamo Elevado ($500,001-$2,000,000) por Tipo de Empleo')
plt.xlabel('Tipo de Empleo')
plt.ylabel('Cantidad de Clientes')
plt.legend(title='Elegibilidad')
plt.savefig('loan_eligibility_large_by_employment_april2025.png')
plt.show()


# Matriz de correlación
# Definir explícitamente el orden de las columnas numéricas
numeric_cols = [
    'ID_Cliente',
    'Edad',
    'Ingresos_Mensuales',
    'Años_Empleo',
    'Puntuacion_Crediticia',
    'Deuda_Actual',
    'Monto_Prestamo_Solicitado',
    'Ratio_Deuda_Ingresos',
    'Apto_Prestamo_Pequeño',
    'Apto_Prestamo_Mediano',
    'Apto_Prestamo_Elevado'
]

# Seleccionar las columnas numéricas en el orden definido
numeric_df = df[numeric_cols]

# Renombrar las columnas para eliminar guiones bajos (para el mapa de calor y el CSV)
numeric_df = numeric_df.rename(columns={
    'ID_Cliente': 'ID Cliente',
    'Edad': 'Edad',
    'Ingresos_Mensuales': 'Ingresos Mensuales',
    'Años_Empleo': 'Años Empleo',
    'Puntuacion_Crediticia': 'Puntuación Crediticia',
    'Deuda_Actual': 'Deuda Actual',
    'Monto_Prestamo_Solicitado': 'Monto Préstamo Solicitado',
    'Ratio_Deuda_Ingresos': 'Ratio Deuda Ingresos',
    'Apto_Prestamo_Pequeño': 'Apto Préstamo Pequeño',
    'Apto_Prestamo_Mediano': 'Apto Préstamo Mediano',
    'Apto_Prestamo_Elevado': 'Apto Préstamo Elevado'
})

# Calcular la matriz de correlación
correlation_matrix = numeric_df.corr()

# Matriz de correlación sin guiones
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación (Feb-Abr 2025)')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('correlation_matrix_feb_apr2025.png', bbox_inches='tight')
plt.show()

# Exportar la matriz de correlación a CSV
correlation_matrix.to_csv('correlation_matrix.csv', encoding='utf-8-sig', index=True)