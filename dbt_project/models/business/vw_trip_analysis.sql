
{{
    config(
        materialized = 'view',
        schema = 'business'
    )
}}

SELECT
    t.trip_id,
    t.customer_id,
    c.full_name AS customer_name,
    t.driver_id,
    d.full_name AS driver_name,
    t.vehicle_id,
    t.trip_start_time,
    t.trip_end_time,
    t.start_location,
    t.end_location,
    t.distance_km,
    t.fare_amount,
    t.payment_method,
    t.trip_status

FROM {{ ref('FactTrips') }} t

LEFT JOIN {{ ref('DimCustomer') }} c
    ON t.customer_id = c.customer_id

LEFT JOIN {{ ref('DimDrivers') }} d
    ON t.driver_id = d.driver_id
