# Loan Analysis in Argentina (April 2025)

Freelance project to evaluate loan eligibility in the Argentine market, adjusted for April 2025 inflation (2.7% monthly, 11.5% accumulated). March inflation (3.7%) was anomalous due to the school cycle, reflecting a stabilized economic context in April.

## Objective
Determine which fictitious client profiles are eligible for loans based on income ($165,483-$2,787,500), employment type (~40% informal/unemployed), credit score, and debt-to-income ratio. The project simulates an analysis for Argentine fintechs (e.g., Ualá, Mercado Pago), optimizing loan approvals.

## Economic Context
- **Inflation**: March 2025 (3.7%, high due to school cycle), April 2025 (2.7%, REM projection), 2025 accumulated (11.5%).
- **Salaries** (private sector, April 2025):
  - Minimum: $165,483 (50% SMVM, informal).
  - Average: $1,314,501 (RIPTE adjusted).
  - Maximum: $2,787,500 (tech, mining).
- **Impact**: Basic basket (~$1,127,000) limits borrowing capacity, justifying strict thresholds (income >$557,500, debt-to-income ratio <30%).

## Methodology
- **Tools**:
  - Python (pandas, numpy, sklearn, seaborn, matplotlib).
  - SQL (SQLite).
  - Tableau Public (future visualizations).
- **Steps**:
  1. Generate fictitious dataset of 1,000 clients.
  2. Initial exploration (EDA) with graphs and SQL queries.
  3. Predictive modeling (logistic regression, in progress).
  4. Visualization in Tableau Public (pending).
  5. Conclusions and recommendations for fintechs.

## Progress
- **Dataset**: 1,000 fictitious clients with incomes ($165,483-$2,787,500), ~30% informal, ~20-30% loan-eligible ([clientes_ficticios_abril2025.csv]).
- **Exploration**:
  - Graphs: Income distribution ([income_distribution_april2025.png]), loan eligibility by employment ([loan_eligibility_by_employment_april2025.png]), correlation ([correlation_matrix_april2025.png]).
  - SQL: Average incomes (Formal ~$1,800,000, Informal ~$450,000), eligibility by age (~30% in 25-55 years).
- **Code**: [generate_data.py], [explore_data.py], [run_sql.py], [queries.sql].

## Repository Structure


/prestamos-argentina
├── .gitignore                    # Ignores unnecessary files
├── README.md
├── clientes_ficticios_abril2025.csv  # Dataset (in Spanish)
├── generate_data.py              # Data generation
├── explore_data.py               # EDA
├── run_sql.py                    # SQL queries execution
├── queries.sql                   # SQL queries
├── income_distribution_april2025.png  # Income graph
├── loan_eligibility_by_employment_april2025.png  # Eligibility graph
├── correlation_matrix_april2025.png  # Correlation graph
