{{ config(
    materialized='table'
) }}

with stg_data as (
    SELECT
        *
    FROM 
        "DOGPIPELINE"."DOGS"."full_data" 
)

SELECT 
    *
FROM
    stg_data