{{ config(
    materialized='table'
) }}

WITH renaming AS (
    SELECT
        veterinarian_id AS vet_id,
        veterinarian_first_name AS vet_first_name,
        veterinarian_last_name AS vet_last_name,
        veterinarian_gender AS vet_gender,
        veterinarian_age AS vet_age,
        specialty_name AS vet_specialization,
        veterinarian_contact AS vet_contact
    FROM 
        {{ref('stg_data')}}
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
    renaming
