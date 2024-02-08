{{ config(
    materialized='incremental',
    unique_key='product_id'
) }}

WITH dim_product AS (
    SELECT
        product_id,
        product_name,
        product_description,
        product_price
     FROM 
        {{ref('inter_product')}}
)

SELECT
    product_id,
    product_name,
    product_description,
    product_price
FROM 
    dim_product
