{{ config(
    materialized='incremental',
    unique_key='appointment_id'
) }}

WITH dim_app AS (
    SELECT
        *
    FROM 
        {{ref('inter_appointment')}}
)

SELECT
    appointment_id,
    appointment_date,
    dog_id,
    vet_id,
    appointment_purpose,
    appointment_fees
FROM 
    dim_app
