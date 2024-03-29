{{ config(
    materialized='incremental',
    unique_key= 'transaction_id'
) }}

with dedup as (
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
        dm.product_price,
        ROW_NUMBER() OVER (PARTITION BY transaction_id ORDER BY order_date) AS row_num
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
)

SELECT 
    transaction_id,
    order_id,
    order_date,
    owner_id,
    dog_id,
    vet_id,
    appointment_id,
    product_id,
    quantity,
    subtotal,
    product_price
FROM
    dedup
WHERE
    row_num = 1