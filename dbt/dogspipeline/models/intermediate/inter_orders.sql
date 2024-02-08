{{ config(
    materialized='incremental',
    unique_key= 'transaction_id'
) }}

SELECT
    fl.transaction_id,
    fl.order_id,
    fl.order_date,
    do.owner_id,
    dd.dog_id,
    dv.vet_id,
    da.appointment_id,
    dm.product_id,
    fl.quantity,
    fl.subtotal,
    dm.product_price
FROM
    {{ref('inter_data')}} AS fl
LEFT JOIN 
    {{ref('inter_owner')}} AS do 
        ON fl.owner_id = do.owner_id
LEFT JOIN 
    {{ref('inter_dog')}} AS dd 
        ON fl.dog_id = dd.dog_id
LEFT JOIN 
    {{ref('inter_veterinarian')}} AS dv 
        ON fl.veterinarian_id = dv.vet_id
LEFT JOIN 
    {{ref('inter_appointment')}} AS da 
        ON fl.appointment_id = da.appointment_id
LEFT JOIN 
    {{ref('inter_product')}} AS dm 
        ON fl.product_id = dm.product_id