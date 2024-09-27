{% test checkThreshold(model, column_name) %}
select * from {{ model }} where {{ column_name }} > {{var('conf1'}}
{% endtest %}

 