-- models/intermediate/dim_owner.sql

{{ config(
    materialized='table',
) }}

WITH raw_owner AS (
  SELECT
    owner_id,
    owner_first_name,
    owner_last_name,
    owner_email,
    owner_phone,
    owner_address
  FROM {{ ref('dogpipeline.dogs.full_data') }}
  WHERE owner_id IS NOT NULL
)

SELECT
  owner_id,
  owner_first_name,
  owner_last_name,
  owner_email,
  owner_phone,
  owner_address
FROM raw_owner;
