# Análisis de Préstamos en Argentina (Febrero-Abril 2025)

Proyecto freelance para evaluar la elegibilidad de préstamos en el mercado argentino, ajustado a la inflación de febrero a abril 2025 (2.5%-3.7% mensual, 11.5% acumulada). La inflación de marzo (3.7%) fue anómala por el ciclo escolar, pero se estabilizó en abril (2.7%), reflejando un contexto económico más favorable para préstamos.

## Objetivo

Determinar qué perfiles de clientes ficticios son aptos para préstamos pequeño ($30,000-$100,000), mediano ($100,001-$500,000) y elevado ($500,001-$2,230,000) según ingresos mensuales ($165,483-$2,787,500, promedio Feb-Abr 2025), tipo de empleo (40% informales/desempleados), puntuación crediticia y ratio deuda/ingresos. Los criterios se ajustaron para ser menos exigentes, alineándose con la oferta de préstamos de fintechs argentinas (ej. Ualá, Mercado Pago), optimizando aprobaciones en un contexto donde la mayoría de los clientes tienen ingresos bajos a moderados (~$400,000-$1,200,000).

## Contexto Económico

- **Inflación**:
  - Febrero 2025: 2.5% (estimación REM ajustada).
  - Marzo 2025: 3.7% (alta por ciclo escolar).
  - Abril 2025: 2.7% (proyección REM).
  - Acumulada 2025 (hasta abril): 11.5%.
- **Salarios (sector privado, promedio febrero-abril 2025)**:
  - Mínimo: $165,483 (50% SMVM, informal).
  - Promedio: $1,314,501 (RIPTE ajustado).
  - Máximo: $2,787,500 (tecnología, minería).
  - Distribución: La mayoría de los clientes tienen ingresos entre $165,483 y $1,200,000, con un pico en $400,000-$600,000, y pocos alcanzan el máximo.
- **Impacto**: La canasta básica (~$1,127,000 en abril) limita la capacidad de endeudamiento, pero los criterios menos estrictos (ingresos >$300,000 para préstamo pequeño, ratio deuda/ingresos <0.5) permiten mayor acceso a préstamos, especialmente para clientes con ingresos bajos a moderados.

## Metodología

### Herramientas
- Python (pandas, numpy, sklearn, seaborn, matplotlib).  
- SQL (SQLite).  
- Tableau Public (visualizaciones interactivas).

### Pasos
1. Generar dataset ficticio de 1,000 clientes con ingresos mensuales ajustados al contexto de febrero-abril 2025.  
2. Exploración inicial (EDA) con gráficos y consultas SQL para analizar ingresos, elegibilidad y correlaciones.  
3. Detección de fraude mediante consultas de anomalías (ratios de deuda altos, ingresos inconsistentes).  
4. Modelado predictivo (regresión logística, en progreso).  
5. Visualización en Tableau Public: 2 dashboards interactivos con análisis por tipo de empleo, importancia de características y correlaciones.  

## Progreso

### Dataset
- 1,000 clientes ficticios con ingresos ($165,483-$2,787,500, promedio Feb-Abr 2025), ~30% informales, ~20-30% aptos para préstamos ([clientes_ficticios_abril2025.csv](clientes_ficticios_abril2025.csv)).  
- **Criterios de elegibilidad ajustados**:
  - **Pequeño ($30,000-$100,000)**: Puntuación crediticia >500, ratio deuda/ingresos <0.5, ingresos >$300,000.  
  - **Mediano ($100,001-$500,000)**: Puntuación crediticia >600, ratio deuda/ingresos <0.4, ingresos >$500,000.  
  - **Elevado ($500,001-$2,230,000)**: Puntuación crediticia >700, ratio deuda/ingresos <0.3, ingresos >$1,000,000.

### Exploración
- **Distribución de ingresos**: La mayoría de los clientes tienen ingresos entre $165,483 y $1,200,000, con un pico en $400,000-$600,000, reflejando un mercado con alta proporción de ingresos bajos a moderados ([income_distribution_april2025.png](income_distribution_april2025.png)).
- **Elegibilidad por tipo de empleo**:
  - **Préstamo Pequeño ($30,000-$100,000)**: Formales (~71% aptos), informales (~57%), autónomos (~50%), desempleados (~50%).
  - **Préstamo Mediano ($100,001-$500,000)**: Formales (~71%), autónomos (~44%), informales (~34%), desempleados (~30%).
  - **Préstamo Elevado ($500,001-$2,230,000)**: Formales (~63%), autónomos (~33%), desempleados (~20%), informales (~14%).
  - Visualización: ([loan_eligibility_by_employment_april2025.png](loan_eligibility_by_employment_april2025.png)).
- **Correlaciones**:
  - Puntuación crediticia e ingresos mensuales tienen correlaciones positivas fuertes con la elegibilidad (0.79 y 0.84 para préstamo pequeño).
  - Deuda actual y ratio deuda/ingresos afectan negativamente la aprobación (-0.51 y -0.23).
  - Edad y tipo de empleo tienen correlaciones débiles (~0), indicando menor relevancia ([correlation_matrix_april2025.png](correlation_matrix_april2025.png)).
- **Importancia de características**:
  - Puntuación crediticia (0.51) e ingresos mensuales (0.19) son los factores más relevantes para la aprobación.
  - Tipo de empleo tiene un impacto mínimo (<0.01) ([feature_importance.csv](feature_importance.csv)).
- **SQL**:
  - Ingresos promedio: Formal ~$1,800,000, Informal ~$450,000 (promedio Feb-Abr 2025).
  - Elegibilidad por edad: ~30% en 25-55 años.
  - Detección de fraude: Ratios de deuda altos, ingresos inconsistentes, solicitudes sospechosas.
- **Código**:
  - Generación de datos: [generate_data.py](generate_data.py).  
  - Exploración: [explore_data.py](explore_data.py).  
  - Consultas SQL: [run_sql.py](run_sql.py), [queries.sql](queries.sql).

### Visualización
- **Dashboards en Tableau Desktop**:
  - Dashboard 1: "Análisis de Aptitud para Préstamos - Resumen (Feb-Abr 2025)" – Incluye distribución de ingresos, importancia de características y matriz de correlación. Descarga el archivo de Tableau para explorar: [Resumen_Aptitud_Prestamos.twbx](Summary_Loan_Eligibility.twbx).
  - Dashboard 2: "Análisis de Aptitud para Préstamos - Detalle por Rango (Feb-Abr 2025)" – Incluye análisis de elegibilidad por tipo de empleo para préstamos pequeño, mediano y elevado. Descarga el archivo de Tableau para explorar: [Detalles_Aptitud_Prestamos.twbx](Details_Loan_Eligibility.twbx).
- Nota: Los dashboards pueden visualizarse abriendo los archivos `.twbx` en Tableau Desktop.

## Conclusiones
- **Distribución de ingresos y contexto económico**: La mayoría de los clientes tienen ingresos mensuales entre $165,483 y $1,200,000 (promedio Feb-Abr 2025), con una minoría alcanzando hasta $2,787,500. La inflación de febrero a abril (2.5%-3.7%) y el aumento de la canasta básica (~$1,127,000) limitan la capacidad de endeudamiento, pero los criterios menos exigentes permiten mayor acceso a préstamos pequeños y medianos.
- **Factores clave para la aprobación**: La puntuación crediticia (importancia 0.51) y los ingresos mensuales (0.19) son los principales determinantes de elegibilidad, según el análisis de importancia de características. La deuda actual y el ratio deuda/ingresos tienen un impacto negativo significativo (correlaciones de -0.51 y -0.23 con la aprobación), mientras que el tipo de empleo tiene una influencia mínima (importancia <0.01).
- **Elegibilidad por tipo de préstamo y empleo**:
  - **Préstamo Pequeño ($30,000-$100,000)**: ~20-30% de clientes son aptos, con los formales liderando (~71% aptos), seguidos por informales (~57%), autónomos (~50%) y desempleados (~50%). Los criterios flexibles (ingresos >$300,000, puntuación crediticia >500) hacen que este rango sea accesible para una amplia gama de clientes.
  - **Préstamo Mediano ($100,001-$500,000)**: La aprobación cae (~15-20% aptos), con los formales aún liderando (~71%), pero los informales (~34%), autónomos (~44%) y desempleados (~30%) enfrentan más restricciones debido a ingresos promedio más bajos (~$450,000 para informales).
  - **Préstamo Elevado ($500,001-$2,230,000)**: Solo ~10-15% son aptos, con los formales dominando (~63%), mientras que los informales (~14%), autónomos (~33%) y desempleados (~20%) tienen tasas muy bajas debido a los criterios estrictos (ingresos >$1,000,000, puntuación crediticia >700).
- **Recomendaciones para fintechs**:
  - Priorizar préstamos pequeños para informales y desempleados (~57% y ~50% aptos), ya que son más accesibles y tienen alta demanda en este segmento.
  - Para préstamos medianos, enfocar esfuerzos en clientes formales (~71% aptos) y autónomos (~44%), ajustando estrategias para aumentar la aprobación de informales mediante incentivos (ej. educación financiera para mejorar la puntuación crediticia).
  - Los préstamos elevados deben dirigirse exclusivamente a clientes formales con ingresos altos y puntuaciones crediticias excelentes, ya que otros segmentos tienen tasas de aprobación muy bajas.
  - Usar la puntuación crediticia como filtro principal para todos los rangos, y considerar los ingresos mensuales como un factor secundario clave, especialmente para préstamos medianos y elevados.

## Archivos
- Dataset: [clientes_ficticios_abril2025.csv](clientes_ficticios_abril2025.csv).  
- Gráficos: [income_distribution_feb_apr2025.png](income_distribution_feb_apr2025.png), [loan_eligibility_small_by_employment_april2025.png](loan_eligibility_small_by_employment_april2025.png), [loan_eligibility_medium_by_employment_april2025.png](loan_eligibility_medium_by_employment_april2025.png), [loan_eligibility_large_by_employment_april2025.png](loan_eligibility_large_by_employment_april2025.png),  [correlation_matrix_april2025.png](correlation_matrix_feb_apr2025.png).  
- Código: [generate_data.py](generate_data.py), [explore_data.py](explore_data.py), [run_sql.py](run_sql.py), [queries.sql](queries.sql).  
- Tableau Workbooks: [Resumen_Aptitud_Prestamos.twbx](Resumen_Aptitud_Prestamos.twbx), [Detalle_Aptitud_Prestamos.twbx](Detalle_Aptitud_Prestamos.twbx).
