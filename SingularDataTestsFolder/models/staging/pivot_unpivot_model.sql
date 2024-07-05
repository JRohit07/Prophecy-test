WITH orders AS (

  SELECT * 
  
  FROM {{ ref('orders')}}

),

Reformat_1 AS (

  SELECT 
    ORDER_ID AS ORDER_ID,
    STATUS AS STATUS,
    CUSTOMER_ID AS CUSTOMER_ID
  
  FROM orders AS in0

),

order_status_pivot AS (

  SELECT 
    CUSTOMER_ID AS CUSTOMER_ID,
    "'completed'" AS COMPLETED,
    "'return_pending'" AS RETURN_PENDING,
    "'placed'" AS PLACED,
    "'returned'" AS RETURNED,
    "'shipped'" AS SHIPPED
  
  FROM Reformat_1 AS in0
  PIVOT (
    COUNT(order_id)
    FOR STATUS
    IN (
      'completed', 'return_pending', 'placed', 'returned', 'shipped'
    )
  )

),

Unpivot_2 AS (

  SELECT * 
  
  FROM order_status_pivot AS in02
  UNPIVOT (
    order_count
    FOR order_status IN (
      RETURNED, SHIPPED, COMPLETED, PLACED, RETURN_PENDING
    )
  )

),

reformatted_data_1 AS (

  SELECT * 
  
  FROM Reformat_1 AS in0

),

reformatted_data AS (

  SELECT * 
  
  FROM Reformat_1 AS in0

)

SELECT *

FROM Unpivot_2
