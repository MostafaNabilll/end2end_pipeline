{{ config(
    materialized='view'
) }}

WITH extract_info AS (
    SELECT
        owner_id,
        owner_first_name,
        owner_last_name,
        owner_email,
        owner_phone,
        owner_address,
        REGEXP_SUBSTR(owner_address, '[0-9]+', 1, 2) AS owner_zip_code,
        REGEXP_SUBSTR(owner_address, '[^0-9,]+', 1, 2) AS owner_city
    FROM 
        {{ref('stg_data')}}
)

SELECT
    owner_id,
    owner_first_name,
    owner_last_name,
    owner_email,
    owner_phone,
    owner_address,
    owner_zip_code,
    owner_city
FROM 
    extract_info