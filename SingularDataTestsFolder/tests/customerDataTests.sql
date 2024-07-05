{{
  config({    
    "fail_calc": "count(distinct id)",
    "limit": 10
  })
}}

WITH raw_customers AS (

  SELECT * 
  
  FROM {{ ref('raw_customers')}}

),

Reformat_1 AS (

  SELECT 
    id AS id,
    first_name AS first_name,
    last_name AS last_name
  
  FROM raw_customers AS in0

),

raw_orders AS (

  SELECT * 
  
  FROM {{ ref('raw_orders')}}

),

raw_payments AS (

  SELECT * 
  
  FROM {{ ref('raw_payments')}}

),

Join_1 AS (

  SELECT 
    in0.id AS id,
    in0.first_name AS first_name,
    in0.last_name AS Last_Name,
    in1.status AS status,
    in1.order_date AS order_date,
    in2.order_id AS order_id,
    in2.payment_method AS payment_method,
    in2.amount AS amount,
    in1.user_id AS user_id
  
  FROM Reformat_1 AS in0
  INNER JOIN raw_orders AS in1
     ON in0.id = in1.id
  LEFT JOIN raw_payments AS in2
     ON in0.id = in2.id

)

SELECT *

FROM Join_1
