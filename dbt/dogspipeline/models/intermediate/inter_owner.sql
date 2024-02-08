{{ config(
    materialized='table'
) }}

WITH remove_dups AS (
    SELECT
        owner_id,
        owner_first_name,
        owner_last_name,
        owner_email,
        CASE
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(owner_phone, '[^0-9]', '')), 1, 1) = '0' THEN TRIM(REGEXP_REPLACE(owner_phone, '[^0-9]', ''))
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(owner_phone, '[^0-9]', '')), 1, 2) = '33' THEN '0' || SUBSTRING(TRIM(REGEXP_REPLACE(owner_phone, '[^0-9]', '')), 3)
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(owner_phone, '[^0-9]', '')), 1, 5) = '+33(0)' THEN '0' || SUBSTRING(TRIM(REGEXP_REPLACE(owner_phone, '[^0-9]', '')), 7)
            ELSE '0' || TRIM(REGEXP_REPLACE(owner_phone, '[^0-9]', ''))
        END AS formatted_phone,
        owner_address,
        owner_zip_code,
        owner_city,
        ROW_NUMBER() OVER (PARTITION BY owner_id ORDER BY owner_id) AS row_num
    FROM 
        {{ref('stg_owner')}}
)

SELECT
    owner_id,
    owner_first_name,
    owner_last_name,
    owner_email,
    CASE
        WHEN SUBSTRING(formatted_phone, 1, 2) = '00' THEN '0' || SUBSTRING(formatted_phone, 3)
        WHEN SUBSTRING(formatted_phone, 1, 1) = '0' THEN formatted_phone
        ELSE '0' || formatted_phone
    END AS owner_phone,
    owner_address

FROM 
    remove_dups
WHERE 
    row_num = 1