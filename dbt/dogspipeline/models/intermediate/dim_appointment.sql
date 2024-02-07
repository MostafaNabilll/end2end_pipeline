{{ config(
    materialized='incremental',
    unique_key='appointment_id'
) }}

WITH remove_dups AS (
    SELECT
        appointment_id,
        appointment_date,
        dog_id,
        veterinarian_id,
        appointment_purpose,
        ROW_NUMBER() OVER (PARTITION BY appointment_id ORDER BY appointment_id) AS row_num
    FROM "DOGPIPELINE"."DOGS"."full_data"
)

SELECT
    appointment_id,
    appointment_date,
    dog_id,
    veterinarian_id,
    appointment_purpose
FROM remove_dups
WHERE row_num = 1
