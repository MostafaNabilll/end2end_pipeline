{{ config(
    materialized='incremental',
    unique_key='transaction_id',
    partition_by=['order_date']
) }}

SELECT
    fl.transaction_id,
    fl.order_id,
    fl.order_date,
    dm.product_id,
    fl.quantity,
    fl.subtotal,
    do.owner_id,
    dd.dog_id,
    dv.veterinarian_id,
    da.appointment_id,
    dm.product_price
FROM
    "DOGPIPELINE"."DOGS"."full_data" AS fl
LEFT JOIN "DOGPIPELINE"."DOGS".dim_owner AS do ON fl.owner_id = do.owner_id
LEFT JOIN "DOGPIPELINE"."DOGS".dim_dog AS dd ON fl.dog_id = dd.dog_id
LEFT JOIN "DOGPIPELINE"."DOGS".dim_veterinarian AS dv ON fl.veterinarian_id = dv.veterinarian_id
LEFT JOIN "DOGPIPELINE"."DOGS".dim_appointment AS da ON fl.appointment_id = da.appointment_id
LEFT JOIN "DOGPIPELINE"."DOGS".dim_product AS dm ON fl.product_id = dm.product_id
