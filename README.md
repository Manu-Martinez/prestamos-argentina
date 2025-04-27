# Análisis de Préstamos en Argentina (Abril 2025)

Proyecto freelance para evaluar la elegibilidad de préstamos en el mercado argentino, ajustado a la inflación de abril 2025 (2.7% mensual, 11.5% acumulada). La inflación de marzo (3.7%) fue anómala por el ciclo escolar, reflejando un contexto económico estabilizado en abril.

## Objetivo
Determinar qué perfiles de clientes ficticios son aptos para préstamos según ingresos ($165,483-$2,787,500), tipo de empleo (~40% informales/desempleados), puntuación crediticia y ratio deuda/ingresos. Simula un análisis para fintechs argentinas (ej. Ualá, Mercado Pago), optimizando aprobaciones.

## Contexto Económico
- **Inflación**: Marzo 2025 (3.7%, alta por ciclo escolar), abril 2025 (2.7%, proyección REM), acumulada 2025 (11.5%).
- **Salarios** (sector privado, abril 2025):
  - Mínimo: $165,483 (50% SMVM, informal).
  - Promedio: $1,314,501 (RIPTE ajustado).
  - Máximo: $2,787,500 (tecnología, minería).
- **Impacto**: Canasta básica (~$1,127,000) limita capacidad de endeudamiento, justificando umbrales estrictos (ingresos >$557,500, ratio deuda/ingresos <30%).

## Metodología
- **Herramientas**:
  - Python (pandas, numpy, sklearn, seaborn, matplotlib).
  - SQL (SQLite).
  - Tableau Public (visualizaciones futuras).
- **Pasos**:
  1. Generar dataset ficticio de 1,000 clientes.
  2. Exploración inicial (EDA) con gráficos y consultas SQL.
  3. Detección de fraude mediante consultas de anomalías.
  4. Modelado predictivo (regresión logística, en progreso).
  5. Visualización en Tableau Public (pendiente).
  6. Conclusiones y recomendaciones para fintechs.

## Progreso
- **Dataset**: 1,000 clientes ficticios con ingresos ($165,483-$2,787,500), ~30% informales, ~20-30% aptos para préstamos ([clientes_ficticios_abril2025.csv]).
- **Exploración**:
  - Gráficos: Distribución de ingresos ([income_distribution_april2025.png]), elegibilidad por empleo ([loan_eligibility_by_employment_april2025.png]), correlación ([correlation_matrix_april2025.png]).
  - SQL: Ingresos promedio (Formal ~$1,800,000, Informal ~$450,000), elegibilidad por edad (~30% en 25-55 años), detección de fraude (ratios de deuda altos, ingresos inconsistentes, solicitudes sospechosas).
- **Código**: [generate_data.py], [explore_data.py], [run_sql.py], [queries.sql].

## Estructura del Repositorio

/prestamos-argentina
├── .gitignore                    # Ignora archivos innecesarios
├── README.md
├── clientes_ficticios_abril2025.csv  # Dataset (en español)
├── generate_data.py              # Generación de datos
├── explore_data.py               # EDA
├── run_sql.py                    # Ejecución de consultas SQL
├── queries.sql                   # Consultas SQL (incluye detección de fraude)
