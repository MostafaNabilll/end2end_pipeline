{{ config(
    materialized='incremental',
    unique_key='dog_id'
) }}

WITH dim_dog AS (
    SELECT
        *
    FROM 
        {{ref('inter_dog')}}
)

SELECT
    dog_id,
    owner_id,
    dog_name,
    dog_breed,
    dog_age,
    dog_gender
FROM 
    dim_dog