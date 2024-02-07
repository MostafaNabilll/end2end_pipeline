{{ config(
    materialized='table',
    unique_key='product_id'
) }}

WITH remove_dups AS (
    SELECT
        product_id,
        product_name,
        product_description,
        product_price
     FROM "DOGPIPELINE"."DOGS"."full_data"
)

SELECT
    product_id,
    product_name,
    product_description,
    product_price
FROM remove_dups