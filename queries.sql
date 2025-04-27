-- Query 1: Ingresos promedio por tipo de empleo
SELECT Tipo_Empleo, AVG(Ingresos_Mensuales) as Ingresos_Promedio, COUNT(*) as Cantidad
FROM clientes
GROUP BY Tipo_Empleo;

-- Query 2: Porcentaje de clientes aptos por rango de edad
SELECT 
    CASE 
        WHEN Edad BETWEEN 18 AND 24 THEN '18-24'
        WHEN Edad BETWEEN 25 AND 55 THEN '25-55'
        ELSE '56-70'
    END as Rango_Edad,
    AVG(Apto_Prestamo) * 100 as Porcentaje_Aptos
FROM clientes
GROUP BY Rango_Edad;

-- Query 3: Clientes con ratio deuda/ingresos inusualmente alto (>0.5)
SELECT ID_Cliente, Ingresos_Mensuales, Deuda_Actual, Ratio_Deuda_Ingresos, Tipo_Empleo
FROM clientes
WHERE Ratio_Deuda_Ingresos > 0.5
ORDER BY Ratio_Deuda_Ingresos DESC;

-- Query 4: Ingresos inconsistentes para tipo de empleo (altos para informales/desempleados)
SELECT ID_Cliente, Ingresos_Mensuales, Tipo_Empleo, Puntuacion_Crediticia
FROM clientes
WHERE (Tipo_Empleo IN ('Informal', 'Desempleado') AND Ingresos_Mensuales > 2000000)
ORDER BY Ingresos_Mensuales DESC;

-- Query 5: Puntuación crediticia baja con préstamos altos
SELECT ID_Cliente, Puntuacion_Crediticia, Monto_Prestamo_Solicitado, Ingresos_Mensuales
FROM clientes
WHERE Puntuacion_Crediticia < 500 
    AND Monto_Prestamo_Solicitado > (SELECT AVG(Monto_Prestamo_Solicitado) FROM clientes)
ORDER BY Monto_Prestamo_Solicitado DESC;

-- Query 6: Préstamos solicitados desproporcionados respecto a ingresos
SELECT ID_Cliente, Ingresos_Mensuales, Monto_Prestamo_Solicitado, 
       (Monto_Prestamo_Solicitado / (Ingresos_Mensuales * 12)) as Ratio_Prestamo_Ingreso_Anual
FROM clientes
WHERE (Monto_Prestamo_Solicitado / (Ingresos_Mensuales * 12)) > 0.5
ORDER BY Ratio_Prestamo_Ingreso_Anual DESC;

-- Query 7: Valores atípicos en Deuda_Actual e Ingresos_Mensuales (más de 3 desviaciones estándar)
WITH Stats AS (
    SELECT 
        AVG(Ingresos_Mensuales) as Avg_Ingresos,
        STDDEV(Ingresos_Mensuales) as Std_Ingresos,
        AVG(Deuda_Actual) as Avg_Deuda,
        STDDEV(Deuda_Actual) as Std_Deuda
    FROM clientes
)
SELECT ID_Cliente, Ingresos_Mensuales, Deuda_Actual, Tipo_Empleo
FROM clientes, Stats
WHERE Ingresos_Mensuales > (Avg_Ingresos + 3 * Std_Ingresos)
    OR Ingresos_Mensuales < (Avg_Ingresos - 3 * Std_Ingresos)
    OR Deuda_Actual > (Avg_Deuda + 3 * Std_Deuda)
ORDER BY Deuda_Actual DESC, Ingresos_Mensuales DESC;