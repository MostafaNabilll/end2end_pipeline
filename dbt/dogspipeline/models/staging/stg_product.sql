{{ config(
    materialized='table'
) }}

WITH stg_product AS (
    SELECT
        product_id,
        product_name,
        product_description,
        product_price
     FROM 
        {{ref('stg_data')}}
)

SELECT
    *
FROM 
    stg_product
