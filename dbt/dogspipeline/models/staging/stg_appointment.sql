{{ config(
    materialized='view'
) }}

WITH rename AS (
    SELECT
        appointment_id,
        appointment_date,
        dog_id,
        veterinarian_id as vet_id,
        appointment_purpose,
        fees as appointment_fees
    FROM 
        {{ref('stg_data')}}
)

SELECT
    appointment_id,
    appointment_date,
    dog_id,
    vet_id,
    appointment_purpose,
    appointment_fees
FROM 
    rename