{% test isThresholdReached(model=test_dummy_modle, column_name=customer_id, threshold=10) %}
select * from {{ model }} where {{ column_name }} > {{var('conf1'}} 
{% endtest %}

 