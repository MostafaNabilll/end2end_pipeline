{{ config(
    materialized='table'
) }}

WITH remove_dups AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY dog_id ORDER BY dog_id) AS row_num
    FROM 
        {{ref('stg_dog')}}
)

SELECT
    dog_id,
    owner_id,
    dog_name,
    dog_breed,
    dog_age,
    dog_gender
FROM 
    remove_dups
WHERE 
    row_num = 1