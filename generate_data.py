import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

data = {
    'ID_Cliente': range(1, n+1),
    'Edad': np.random.normal(35, 10, n).astype(int).clip(18, 70),
    'Ingresos_Mensuales': np.random.lognormal(mean=np.log(1314501), sigma=0.5, size=n).clip(165483, 2787500),
    'Tipo_Empleo': np.random.choice(['Formal', 'Informal', 'Autónomo', 'Desempleado'], n, p=[0.5, 0.3, 0.15, 0.05]),
    'Años_Empleo': np.random.exponential(5, n).clip(0, 30),
    'Puntuacion_Crediticia': np.random.normal(650, 100, n).astype(int).clip(300, 850),
    'Deuda_Actual': np.random.lognormal(mean=np.log(334500), sigma=0.7, size=n).clip(0, 5575000),
    'Monto_Prestamo_Solicitado': np.random.lognormal(mean=np.log(557500), sigma=0.5, size=n).clip(55750, 2230000)
}

df = pd.DataFrame(data)
df['Ratio_Deuda_Ingresos'] = df['Deuda_Actual'] / df['Ingresos_Mensuales']
df['Apto_Prestamo'] = ((df['Ingresos_Mensuales'] > 557500) & 
                       (df['Puntuacion_Crediticia'] > 700) & 
                       (df['Ratio_Deuda_Ingresos'] < 0.3) & 
                       (df['Edad'].between(25, 55))).astype(int)

df.to_csv('clientes_ficticios_abril2025.csv', index=False)
print(df.head())
print(df.describe())