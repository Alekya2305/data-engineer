
-- This model ranks merchants by transaction volume

{{ config(materialized='table') }}

select
merchant,
category,
count(*) as transaction_volume,
sum(amount) as total_revenue,
avg(amount) as avg_transaction_amount
from {{ ref('transactions') }}
group by merchant,category
order by total_revenue desc
