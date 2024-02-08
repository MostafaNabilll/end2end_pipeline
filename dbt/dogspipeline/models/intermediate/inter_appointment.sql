{{ config(
    materialized='table'
) }}

WITH remove_dups AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY appointment_id ORDER BY appointment_id) AS row_num
    FROM 
        {{ref('stg_appointment')}}
)

SELECT
    appointment_id,
    appointment_date,
    dog_id,
    vet_id,
    appointment_purpose,
    appointment_fees
FROM 
    remove_dups
WHERE 
    row_num = 1