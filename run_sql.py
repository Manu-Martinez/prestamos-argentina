import sqlite3
import pandas as pd

conn = sqlite3.connect('clientes.db')
df = pd.read_csv('clientes_ficticios_abril2025.csv')
df.to_sql('clientes', conn, if_exists='replace', index=False)

# Query 1: Ingresos promedio por tipo de empleo (feb-mar-abr 2025)
query1 = '''
SELECT Tipo_Empleo, AVG(Ingresos_Mensuales) as Ingresos_Promedio_Feb_Abr_2025, COUNT(*) as Cantidad
FROM clientes
GROUP BY Tipo_Empleo;
'''
print("\nQuery 1: Ingresos promedio por tipo de empleo (Feb-Abr 2025)")
print(pd.read_sql(query1, conn))

# Query 2: Porcentaje de clientes aptos por rango de edad para cada tipo de préstamo
query2 = '''
SELECT 
    CASE 
        WHEN Edad BETWEEN 18 AND 24 THEN '18-24'
        WHEN Edad BETWEEN 25 AND 55 THEN '25-55'
        ELSE '56-70'
    END as Rango_Edad,
    AVG(Apto_Prestamo_Pequeño) * 100 as Porcentaje_Aptos_Pequeño,
    AVG(Apto_Prestamo_Mediano) * 100 as Porcentaje_Aptos_Mediano,
    AVG(Apto_Prestamo_Elevado) * 100 as Porcentaje_Aptos_Elevado
FROM clientes
GROUP BY Rango_Edad;
'''
print("\nQuery 2: Porcentaje de clientes aptos por rango de edad (Feb-Abr 2025)")
print(pd.read_sql(query2, conn))

# Query 3: Clientes con ratio deuda/ingresos inusualmente alto
query3 = '''
SELECT ID_Cliente, Ingresos_Mensuales, Deuda_Actual, Ratio_Deuda_Ingresos, Tipo_Empleo
FROM clientes
WHERE Ratio_Deuda_Ingresos > 0.5
ORDER BY Ratio_Deuda_Ingresos DESC;
'''
print("\nQuery 3: Clientes con ratio deuda/ingresos inusualmente alto")
print(pd.read_sql(query3, conn))

# Query 4: Ingresos inconsistentes para tipo de empleo
query4 = '''
SELECT ID_Cliente, Ingresos_Mensuales, Tipo_Empleo, Puntuacion_Crediticia
FROM clientes
WHERE (Tipo_Empleo IN ('Informal', 'Desempleado') AND Ingresos_Mensuales > 2000000)
ORDER BY Ingresos_Mensuales DESC;
'''
print("\nQuery 4: Ingresos inconsistentes para tipo de empleo")
print(pd.read_sql(query4, conn))

# Query 5: Puntuación crediticia baja con préstamos altos
query5 = '''
SELECT ID_Cliente, Puntuacion_Crediticia, Monto_Prestamo_Solicitado, Ingresos_Mensuales
FROM clientes
WHERE Puntuacion_Crediticia < 500 
    AND Monto_Prestamo_Solicitado > (SELECT AVG(Monto_Prestamo_Solicitado) FROM clientes)
ORDER BY Monto_Prestamo_Solicitado DESC;
'''
print("\nQuery 5: Puntuación crediticia baja con préstamos altos")
print(pd.read_sql(query5, conn))

# Query 6: Préstamos solicitados desproporcionados (umbral ajustado a 0.1)
query6 = '''
SELECT ID_Cliente, Ingresos_Mensuales, Monto_Prestamo_Solicitado, 
       (Monto_Prestamo_Solicitado / (Ingresos_Mensuales * 12)) as Ratio_Prestamo_Ingreso_Anual
FROM clientes
WHERE (Monto_Prestamo_Solicitado / (Ingresos_Mensuales * 12)) > 0.1
ORDER BY Ratio_Prestamo_Ingreso_Anual DESC;
'''
print("\nQuery 6: Préstamos solicitados desproporcionados (umbral 10% ingreso anual)")
print(pd.read_sql(query6, conn))

# Query 7: Valores atípicos en Deuda_Actual e Ingresos_Mensuales (desviación estándar manual)
query7 = '''
WITH Stats AS (
    SELECT 
        AVG(Ingresos_Mensuales) as Avg_Ingresos,
        SQRT(AVG(Ingresos_Mensuales * Ingresos_Mensuales) - AVG(Ingresos_Mensuales) * AVG(Ingresos_Mensuales)) as Std_Ingresos,
        AVG(Deuda_Actual) as Avg_Deuda,
        SQRT(AVG(Deuda_Actual * Deuda_Actual) - AVG(Deuda_Actual) * AVG(Deuda_Actual)) as Std_Deuda
    FROM clientes
)
SELECT ID_Cliente, Ingresos_Mensuales, Deuda_Actual, Tipo_Empleo
FROM clientes, Stats
WHERE Ingresos_Mensuales > (Avg_Ingresos + 3 * Std_Ingresos)
    OR Ingresos_Mensuales < (Avg_Ingresos - 3 * Std_Ingresos)
    OR Deuda_Actual > (Avg_Deuda + 3 * Std_Deuda)
ORDER BY Deuda_Actual DESC, Ingresos_Mensuales DESC;
'''
print("\nQuery 7: Valores atípicos en Deuda_Actual e Ingresos_Mensuales")
print(pd.read_sql(query7, conn))

conn.close()