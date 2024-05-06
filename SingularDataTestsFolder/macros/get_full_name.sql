{% macro get_full_name(customer, first_name, last_name) %}

                    select
                        {{ customer }}.*,
                        concat({{ first_name }}, ' ', {{ last_name }}) as full_name
                    from {{ customer }}
{% endmacro %}

 