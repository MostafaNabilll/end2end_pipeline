{{ config(
    materialized='table'
) }}

WITH remove_dups AS (
    SELECT
        vet_id,
        vet_first_name,
        vet_last_name,
        vet_gender,
        vet_age,
        vet_specialization,
        CASE
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(vet_contact, '[^0-9]', '')), 1, 1) = '0' THEN TRIM(REGEXP_REPLACE(vet_contact, '[^0-9]', ''))
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(vet_contact, '[^0-9]', '')), 1, 2) = '33' THEN '0' || SUBSTRING(TRIM(REGEXP_REPLACE(vet_contact, '[^0-9]', '')), 3)
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(vet_contact, '[^0-9]', '')), 1, 5) = '+33(0)' THEN '0' || SUBSTRING(TRIM(REGEXP_REPLACE(vet_contact, '[^0-9]', '')), 7)
            ELSE '0' || TRIM(REGEXP_REPLACE(vet_contact, '[^0-9]', ''))
        END AS vet_contact,
        ROW_NUMBER() OVER (PARTITION BY vet_id ORDER BY vet_id) AS row_num
    FROM 
        {{ref('stg_veterinarian')}}
)

SELECT
    vet_id,
    vet_first_name,
    vet_last_name,
    vet_gender,
    vet_age,
    vet_specialization,
    CASE
        WHEN SUBSTRING(vet_contact, 1, 2) = '00' THEN '0' || SUBSTRING(vet_contact, 3)
        WHEN SUBSTRING(vet_contact, 1, 1) = '0' THEN vet_contact
        ELSE '0' || vet_contact
    END AS vet_contact
FROM 
    remove_dups
WHERE 
    row_num = 1