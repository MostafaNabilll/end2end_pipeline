{{ config(
    materialized='table'
) }}

with inter_data as (
    SELECT
        *
    FROM 
        {{ref('stg_data')}}
)

SELECT 
    *
FROM
    inter_data