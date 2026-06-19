-- This model analyzes fraud patterns by category

{{ config(materialized='table') }}

select
category,
count(*) as total_transactions,
sum(case when is_fraud=True then 1 else 0 end) as fruad_count,
round((sum(case when is_fraud=True then 1 else 0 end) * 100.0)/count(*),2) as fraud_rate_pct
from {{ ref('transactions') }}
group by category
order by fraud_rate_pct desc