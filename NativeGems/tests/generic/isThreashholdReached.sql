{% test isThreashholdReached(model, column_name, threshold=10) %}
select * from {{ model }} where {{ column_name }} > {{ threshold }}
{% endtest %}

 