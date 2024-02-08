{{ config(
    materialized='view'
) }}

WITH stg_dog AS (
    SELECT
        dog_id,
        owner_id,
        dog_name,
        dog_breed,
        dog_age,
        dog_gender
    FROM 
        {{ref('stg_data')}}
)

SELECT
    *
FROM 
    stg_dog
