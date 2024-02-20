{{ config(
    materialized='incremental',
    unique_key='owner_id'
) }}

WITH dim_owner AS (
    SELECT
        *
    FROM 
        {{ref('inter_owner')}}
)

SELECT
    owner_id,
    owner_first_name,
    owner_last_name,
    owner_age,
    owner_email,
    owner_phone,
    owner_address,
    owner_zip_code,
    owner_city
FROM 
    dim_owner
