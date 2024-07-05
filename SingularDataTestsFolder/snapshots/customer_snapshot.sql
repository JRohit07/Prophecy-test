{% snapshot customer_snapshot %}
{{
  config({    
    "strategy": 'timestamp',
    "target_database": "JAFFLE_SHOP",
    "target_schema": "SNAPSHOT",
    "unique_key": "ORDER_ID",
    "updated_at": "ORDER_DATE"
  })
}}

WITH orders AS (

  SELECT *
  
  FROM {{ ref('orders')}}

)

SELECT *

FROM orders

{% endsnapshot %}
