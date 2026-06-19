{{ config(materialized='table') }}

select
    transaction_id,
    user_id,
    amount,
    merchant,
    category,
    timestamp,
    is_fraud
from bank_pipeline.transactions