
-- This model calculates total transactions and revenue per day

{{ config(materialized='table') }}

select
date(timestamp) as transaction_date,
count(*) as total_transactions,
sum(amount) as total_revenue,
avg(amount) as avg_transaction_amount,
sum(case when is_fraud=True then 1 else 0 end) as fruad_count
from {{ ref('transactions') }}
group by date(timestamp)
order by transaction_date