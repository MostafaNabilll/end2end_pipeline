{{ config(
    materialized='incremental',
    unique_key='dog_id',
) }}

-- Incremental Model for Numbered Owners
WITH remove_dups AS (
    SELECT
        dog_id,
        owner_id,
        dog_name,
        dog_breed,
        dog_age,
        dog_gender,
        ROW_NUMBER() OVER (PARTITION BY dog_id ORDER BY dog_id) AS row_num
    FROM "DOGPIPELINE"."DOGS"."full_data"
)

SELECT
    dog_id,
    owner_id,
    dog_name,
    dog_breed,
    dog_age,
    dog_gender
FROM remove_dups
WHERE row_num = 1