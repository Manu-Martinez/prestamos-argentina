# Loan Eligibility Analysis in Argentina (February-April 2025)

Freelance project to assess loan eligibility in the Argentine market, adjusted to the inflation rates from February to April 2025 (2.5%-3.7% monthly, 11.5% cumulative). March inflation (3.7%) was anomalous due to the school cycle, but it stabilized in April (2.7%), reflecting a more favorable economic context for loans.

## Objective

Determine which fictitious client profiles are eligible for small ($30,000-$100,000), medium ($100,001-$500,000), and large ($500,001-$2,230,000) loans based on monthly income ($165,483-$2,787,500, Feb-Apr 2025 average), employment type (40% informal/unemployed), credit score, and debt-to-income ratio. Eligibility criteria were relaxed to align with the loan offerings of Argentine fintechs (e.g., Ualá, Mercado Pago), optimizing approvals in a context where most clients have low to moderate incomes (~$400,000-$1,200,000).

## Economic Context

- **Inflation**:
  - February 2025: 2.5% (adjusted REM estimate).
  - March 2025: 3.7% (high due to school cycle).
  - April 2025: 2.7% (REM projection).
  - Cumulative 2025 (up to April): 11.5%.
- **Salaries (private sector, Feb-Apr 2025 average)**:
  - Minimum: $165,483 (50% SMVM, informal).
  - Average: $1,314,501 (adjusted RIPTE).
  - Maximum: $2,787,500 (technology, mining).
  - Distribution: Most clients have incomes between $165,483 and $1,200,000, peaking at $400,000-$600,000, with few reaching the maximum.
- **Impact**: The basic basket (~$1,127,000 in April) limits borrowing capacity, but relaxed criteria (income >$300,000 for small loans, debt-to-income ratio <0.5) enable greater access to loans, especially for clients with low to moderate incomes.

## Methodology

### Tools
- Python (pandas, numpy, sklearn, seaborn, matplotlib).  
- SQL (SQLite).  
- Tableau Public (interactive visualizations).

### Steps
1. Generate a fictitious dataset of 1,000 clients with monthly incomes adjusted to the Feb-Apr 2025 context.  
2. Initial exploration (EDA) with charts and SQL queries to analyze income, eligibility, and correlations.  
3. Fraud detection through anomaly queries (high debt ratios, inconsistent incomes).  
4. Predictive modeling (logistic regression, in progress).  
5. Visualization in Tableau Public: 2 interactive dashboards with analysis by employment type, feature importance, and correlations.

## Progress

### Dataset
- 1,000 fictitious clients with incomes ($165,483-$2,787,500, Feb-Apr 2025 average), ~30% informal, ~20-30% eligible for loans ([clientes_ficticios_abril2025.csv](fictitious_clients_april2025.csv)).  
- **Adjusted eligibility criteria**:
  - **Small ($30,000-$100,000)**: Credit score >500, debt-to-income ratio <0.5, income >$300,000.  
  - **Medium ($100,001-$500,000)**: Credit score >600, debt-to-income ratio <0.4, income >$500,000.  
  - **Large ($500,001-$2,230,000)**: Credit score >700, debt-to-income ratio <0.3, income >$1,000,000.

### Exploration
- **Income Distribution**: Most clients have incomes between $165,483 and $1,200,000, peaking at $400,000-$600,000, reflecting a market with a high proportion of low to moderate incomes ([income_distribution_april2025.png](income_distribution_april2025.png)).
- **Eligibility by Employment Type**:
  - **Small Loan ($30,000-$100,000)**: Formal (~71% eligible), informal (~57%), self-employed (~50%), unemployed (~50%) ([loan_eligibility_small_by_employment_april2025.png](loan_eligibility_small_by_employment_april2025.png)).
  - **Medium Loan ($100,001-$500,000)**: Formal (~71%), self-employed (~44%), informal (~34%), unemployed (~30%) ([loan_eligibility_medium_by_employment_april2025.png](loan_eligibility_medium_by_employment_april2025.png)).
  - **Large Loan ($500,001-$2,230,000)**: Formal (~63%), self-employed (~33%), unemployed (~20%), informal (~14%) ([loan_eligibility_large_by_employment_april2025.png](loan_eligibility_large_by_employment_april2025.png)).
- **Correlations**:
  - Credit score and monthly income have strong positive correlations with eligibility (0.79 and 0.84 for small loans).
  - Current debt and debt-to-income ratio negatively impact approval (-0.51 and -0.23).
  - Age and employment type have weak correlations (~0), indicating lesser relevance ([correlation_matrix_april2025.png](correlation_matrix_april2025.png)).
- **Feature Importance**:
  - Credit score (0.51) and monthly income (0.19) are the most relevant factors for approval.
  - Employment type has minimal impact (<0.01) ([feature_importance.csv](feature_importance.csv)).
- **SQL**:
  - Average income: Formal ~$1,800,000, Informal ~$450,000 (Feb-Apr 2025 average).
  - Eligibility by age: ~30% in 25-55 years.
  - Fraud detection: Identified clients with high debt-to-income ratios (>0.5), inconsistent incomes, and suspicious applications.
- **Code**:
  - Data generation: [generate_data.py](generate_data.py).  
  - Exploration: [explore_data.py](explore_data.py).  
  - SQL queries: [run_sql.py](run_sql.py), [queries.sql](queries.sql).

### Visualization
- **Tableau Dashboards**:
  - Dashboard 1: "Loan Eligibility Analysis - Summary (Feb-Apr 2025)" – Includes income distribution, feature importance, and correlation matrix. Download the Tableau Workbook to explore: [Summary_Loan_Eligibility.twbx](Summary_Loan_Eligibility.twbx).
  - Dashboard 2: "Loan Eligibility Analysis - Details by Range (Feb-Apr 2025)" – Includes eligibility analysis by employment type for small, medium, and large loans. Download the Tableau Workbook to explore: [Details_Loan_Eligibility.twbx](Details_Loan_Eligibility.twbx).
- Note: Dashboards can be viewed by opening the `.twbx` files in Tableau Desktop. 


## Conclusions
- **Income Distribution and Economic Context**: Most clients have monthly incomes between $165,483 and $1,200,000 (Feb-Apr 2025 average), with a minority reaching up to $2,787,500. Inflation from February to April (2.5%-3.7%) and the rising cost of the basic basket (~$1,127,000) limit borrowing capacity, but relaxed criteria enable greater access to small and medium loans.
- **Key Factors for Approval**: Credit score (importance 0.51) and monthly income (0.19) are the primary determinants of eligibility, according to feature importance analysis. Current debt and debt-to-income ratio have a significant negative impact (correlations of -0.51 and -0.23 with approval), while employment type has minimal influence (importance <0.01).
- **Eligibility by Loan Type and Employment**:
  - **Small Loan ($30,000-$100,000)**: ~20-30% of clients are eligible, with formal clients leading (~71% eligible), followed by informal (~57%), self-employed (~50%), and unemployed (~50%). Relaxed criteria (income >$300,000, credit score >500) make this range accessible to a wide range of clients.
  - **Medium Loan ($100,001-$500,000)**: Approval drops (~15-20% eligible), with formal clients still leading (~71%), but informal (~34%), self-employed (~44%), and unemployed (30%) face more restrictions due to lower average incomes ($450,000 for informal).
  - **Large Loan ($500,001-$2,230,000)**: Only ~10-15% are eligible, with formal clients dominating (~63%), while informal (~14%), self-employed (~33%), and unemployed (~20%) have very low rates due to strict criteria (income >$1,000,000, credit score >700).
- **Recommendations for Fintechs**:
  - Prioritize small loans for informal and unemployed clients (~57% and ~50% eligible), as they are more accessible and in high demand in this segment.
  - For medium loans, focus efforts on formal (~71% eligible) and self-employed (~44%) clients, adjusting strategies to increase informal approvals through incentives (e.g., financial education to improve credit scores).
  - Large loans should target only formal clients with high incomes and excellent credit scores, as other segments have very low approval rates.
  - Use credit score as the primary filter for all ranges, and consider monthly income as a key secondary factor, especially for medium and large loans.

## Files
- Dataset: [clientes_ficticios_abril2025.csv](clientes_ficticios_abril2025.csv).  
- Charts: [income_distribution_april2025.png](income_distribution_april2025.png), [loan_eligibility_small_by_employment_april2025.png](loan_eligibility_small_by_employment_april2025.png), [loan_eligibility_medium_by_employment_april2025.png](loan_eligibility_medium_by_employment_april2025.png), [loan_eligibility_large_by_employment_april2025.png](loan_eligibility_large_by_employment_april2025.png), [correlation_matrix_april2025.png](correlation_matrix_april2025.png).  
- Code: [generate_data.py](generate_data.py), [explore_data.py](explore_data.py), [run_sql.py](run_sql.py), [queries.sql](queries.sql).  
- Tableau Workbooks: [Summary_Loan_Eligibility.twbx](Summary_Loan_Eligibility.twbx), [Details_Loan_Eligibility.twbx](Details_Loan_Eligibility.twbx).
