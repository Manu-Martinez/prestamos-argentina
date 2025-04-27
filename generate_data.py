import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

data = {
    'ID_Cliente': range(1, n+1),
    'Edad': np.random.normal(35, 10, n).astype(int).clip(18, 70),
    'Ingresos_Mensuales': np.random.lognormal(mean=np.log(1274734), sigma=0.5, size=n).clip(160567, 2702617),
    'Tipo_Empleo': np.random.choice(['Formal', 'Informal', 'Autónomo', 'Desempleado'], n, p=[0.5, 0.3, 0.15, 0.05]),
    'Años_Empleo': np.random.exponential(5, n).clip(0, 30),
    'Puntuacion_Crediticia': np.random.normal(650, 100, n).astype(int).clip(300, 850),
    'Deuda_Actual': np.random.lognormal(mean=np.log(334500), sigma=0.7, size=n).clip(0, 5575000),
    'Monto_Prestamo_Solicitado': np.random.lognormal(mean=np.log(557500), sigma=0.5, size=n).clip(55750, 2230000)
}

df = pd.DataFrame(data)
df['Ratio_Deuda_Ingresos'] = df['Deuda_Actual'] / df['Ingresos_Mensuales']

# Ajustar criterios de elegibilidad con los nuevos ingresos
# Préstamo pequeño ($30,000-$100,000, plazo 3-6 meses)
df['Apto_Prestamo_Pequeño'] = ((df['Ingresos_Mensuales'] > 160567) &  # Mínimo ajustado
                               (df['Puntuacion_Crediticia'] > 500) &
                               (df['Ratio_Deuda_Ingresos'] < 0.5) &
                               (df['Edad'].between(18, 70))).astype(int)

# Préstamo mediano ($100,001-$500,000, plazo 6-12 meses)
df['Apto_Prestamo_Mediano'] = ((df['Ingresos_Mensuales'] > 300000) &
                               (df['Puntuacion_Crediticia'] > 600) &
                               (df['Ratio_Deuda_Ingresos'] < 0.4) &
                               (df['Edad'].between(20, 65))).astype(int)

# Préstamo elevado ($500,001-$2,000,000, plazo 12-36 meses)
df['Apto_Prestamo_Elevado'] = ((df['Ingresos_Mensuales'] > 557500) &
                               (df['Puntuacion_Crediticia'] > 650) &
                               (df['Ratio_Deuda_Ingresos'] < 0.35) &
                               (df['Edad'].between(25, 55))).astype(int)

df.to_csv('clientes_ficticios_abril2025.csv', index=False)
print(df.head())
print(df.describe())