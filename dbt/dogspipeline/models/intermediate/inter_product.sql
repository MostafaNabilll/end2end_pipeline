{{ config(
    materialized='table'
) }}

WITH remove_dups AS (
    SELECT
        product_id,
        product_name,
        product_description,
        product_price,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY product_id) AS row_num
     FROM 
        {{ref('stg_product')}}
)

SELECT
    product_id,
    product_name,
    product_description,
    product_price
FROM 
    remove_dups
where 
    row_num = 1