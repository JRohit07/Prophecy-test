WITH seed AS (

  SELECT * 
  
  FROM {{ ref('seed')}}

),

seed_data AS (

  SELECT 
    customer_id AS customer_id,
    last_name AS last_name,
    phone AS phone,
    first_name AS first_name,
    country_code AS country_code,
    email AS email,
    account_open_date AS account_open_date,
    account_flags AS account_flags
  
  FROM seed AS in0

)

SELECT *

FROM seed
