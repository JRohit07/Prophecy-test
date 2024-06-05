WITH orders_dataset_db_1 AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.qa_database', 'orders_dataset_db_1') }}

),

orders AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.qa_database', 'orders') }}

),

by_ORDER_DATE AS (

  SELECT 
    orders_dataset_db_1.order_id AS order_id,
    orders_dataset_db_1.customer_id AS customer_id,
    orders_dataset_db_1.order_status AS order_status,
    orders_dataset_db_1.order_category AS order_category,
    orders_dataset_db_1.amount AS amount,
    orders.ID AS ID,
    orders.USER_ID AS USER_ID,
    orders.ORDER_DATE AS ORDER_DATE,
    orders.STATUS AS STATUS
  
  FROM orders
  INNER JOIN orders_dataset_db_1
     ON orders.ORDER_DATE = orders_dataset_db_1.order_date

)

SELECT *

FROM by_ORDER_DATE
