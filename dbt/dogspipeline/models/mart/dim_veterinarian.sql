{{ config(
    materialized='incremental',
    unique_key='vet_id'
) }}

WITH dim_veterinarian AS (
    SELECT
        vet_id,
        vet_first_name,
        vet_last_name,
        vet_gender,
        vet_age,
        vet_specialization,
        vet_contact
    FROM 
        {{ref('inter_veterinarian')}}
)

SELECT
    vet_id,
    vet_first_name,
    vet_last_name,
    vet_gender,
    vet_age,
    vet_specialization,
    vet_contact
FROM 
    dim_veterinarian
