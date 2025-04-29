import pandas as pd
import numpy as np

# Configurar semilla para reproducibilidad
np.random.seed(42)
n_samples = 1000

# Generar datos ficticios
# Edad (18 a 70 años)
edad = np.random.randint(18, 71, size=n_samples)

# Ingresos Mensuales (distribución lognormal ajustada para pesos argentinos en 2025)
ingresos_base = np.random.lognormal(mean=6.559, sigma=0.5, size=n_samples)
ingresos_mensuales = np.round(ingresos_base * 1000).astype(int)  # Redondear a enteros

# Años de empleo (0 a 40 años)
anos_empleo = np.random.randint(0, 41, size=n_samples)

# Puntuación crediticia (300 a 850)
puntuacion_crediticia = np.random.randint(300, 851, size=n_samples)

# Deuda actual (distribución sesgada, 0 a 5,575,000)
deuda_actual = np.random.exponential(scale=500000, size=n_samples)
deuda_actual = np.round(np.clip(deuda_actual, 0, 5575000)).astype(int)  # Redondear a enteros

# Monto del préstamo solicitado (55,750 a 2,230,000)
monto_prestamo_solicitado = np.random.uniform(55750, 2230000, size=n_samples)
monto_prestamo_solicitado = np.round(monto_prestamo_solicitado).astype(int)  # Redondear a enteros

# Ratio deuda/ingresos (0 a 0.5)
ratio_deuda_ingresos = np.random.uniform(0, 0.5, size=n_samples)

# Tipo de empleo (Formal, Informal, Autónomo, Desempleado)
tipo_empleo = np.random.choice(['Formal', 'Informal', 'Autónomo', 'Desempleado'], 
                               size=n_samples, 
                               p=[0.4, 0.3, 0.2, 0.1])

# Elegibilidad para préstamos
apto_prestamo_pequeño = (puntuacion_crediticia > 500) & (ratio_deuda_ingresos < 0.5) & (ingresos_mensuales > 300000)
apto_prestamo_mediano = (puntuacion_crediticia > 600) & (ratio_deuda_ingresos < 0.4) & (ingresos_mensuales > 500000)
apto_prestamo_elevado = (puntuacion_crediticia > 700) & (ratio_deuda_ingresos < 0.3) & (ingresos_mensuales > 1000000)

# Convertir booleanos a enteros (0 o 1)
apto_prestamo_pequeño = apto_prestamo_pequeño.astype(int)
apto_prestamo_mediano = apto_prestamo_mediano.astype(int)
apto_prestamo_elevado = apto_prestamo_elevado.astype(int)

# Crear DataFrame
data = {
    'ID_Cliente': range(1, n_samples + 1),
    'Edad': edad,
    'Ingresos_Mensuales': ingresos_mensuales,
    'Años_Empleo': anos_empleo,
    'Puntuacion_Crediticia': puntuacion_crediticia,
    'Deuda_Actual': deuda_actual,
    'Monto_Prestamo_Solicitado': monto_prestamo_solicitado,
    'Ratio_Deuda_Ingresos': ratio_deuda_ingresos,
    'Tipo_Empleo': tipo_empleo,
    'Apto_Prestamo_Pequeño': apto_prestamo_pequeño,
    'Apto_Prestamo_Mediano': apto_prestamo_mediano,
    'Apto_Prestamo_Elevado': apto_prestamo_elevado
}

df = pd.DataFrame(data)

# Guardar el dataset original
df.to_csv('clientes_ficticios_abril2025.csv', index=False, encoding='utf-8')

# Renombrar columnas para Tableau (sin guiones bajos)
df = df.rename(columns={
    'ID_Cliente': 'ID Cliente',
    'Edad': 'Edad',
    'Ingresos_Mensuales': 'Ingresos Mensuales',
    'Años_Empleo': 'Años Empleo',
    'Puntuacion_Crediticia': 'Puntuación Crediticia',
    'Deuda_Actual': 'Deuda Actual',
    'Monto_Prestamo_Solicitado': 'Monto Prestamo Solicitado',
    'Ratio_Deuda_Ingresos': 'Ratio Deuda Ingresos',
    'Tipo_Empleo': 'Tipo Empleo',
    'Apto_Prestamo_Pequeño': 'Apto Prestamo Pequeño',
    'Apto_Prestamo_Mediano': 'Apto Prestamo Mediano',
    'Apto_Prestamo_Elevado': 'Apto Prestamo Elevado'
})

# Guardar versión ajustada para Tableau
df.to_csv('clientes_ficticios_abril2025_tableau.csv', index=False, encoding='utf-8')