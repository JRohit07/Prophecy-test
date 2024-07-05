{{
  config({    
    "enabled": true,
    "fail_calc": "count(*)",
    "limit": 20,
    "meta": {  },
    "severity": 'warn'
  })
}}

WITH emptySeed AS (

  SELECT * 
  
  FROM {{ ref('emptySeed')}}

),

raw_customers AS (

  SELECT * 
  
  FROM {{ ref('raw_customers')}}

)

SELECT *

FROM raw_customers
