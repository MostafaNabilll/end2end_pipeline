{{ config(
    materialized='table',
    unique_key='veterinarian_id'
) }}

WITH remove_dups AS (
    SELECT
        veterinarian_id,
        veterinarian_first_name,
        veterinarian_last_name,
        veterinarian_gender,
        veterinarian_age,
        specialty_name,
        CASE
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(veterinarian_contact, '[^0-9]', '')), 1, 1) = '0' THEN TRIM(REGEXP_REPLACE(veterinarian_contact, '[^0-9]', ''))
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(veterinarian_contact, '[^0-9]', '')), 1, 2) = '33' THEN '0' || SUBSTRING(TRIM(REGEXP_REPLACE(veterinarian_contact, '[^0-9]', '')), 3)
            WHEN SUBSTRING(TRIM(REGEXP_REPLACE(veterinarian_contact, '[^0-9]', '')), 1, 5) = '+33(0)' THEN '0' || SUBSTRING(TRIM(REGEXP_REPLACE(veterinarian_contact, '[^0-9]', '')), 7)
            ELSE '0' || TRIM(REGEXP_REPLACE(veterinarian_contact, '[^0-9]', ''))
        END AS veterinarian_contact,
        ROW_NUMBER() OVER (PARTITION BY veterinarian_id ORDER BY veterinarian_id) AS row_num
    FROM "DOGPIPELINE"."DOGS"."full_data"
)

SELECT
    veterinarian_id,
    veterinarian_first_name,
    veterinarian_last_name,
    veterinarian_gender,
    veterinarian_age,
    specialty_name,
    CASE
        WHEN SUBSTRING(veterinarian_contact, 1, 2) = '00' THEN '0' || SUBSTRING(veterinarian_contact, 3)
        WHEN SUBSTRING(veterinarian_contact, 1, 1) = '0' THEN veterinarian_contact
        ELSE '0' || veterinarian_contact
    END AS veterinarian_contact
FROM remove_dups
WHERE row_num = 1