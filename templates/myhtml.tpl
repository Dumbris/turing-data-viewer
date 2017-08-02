{% extends "html.tpl" %}
{% macro cell(c, class_='', colspan=0) -%}
    <{{ c.type }} id="T_{{ uuid }}{{ c.id }}" colspan={{ colspan }} class="{{ c.class }} {{ class_ }}" {{ c.attributes|join(" ") }}>{{ c.display_value }}</{{ c.type }}>
{%- endmacro %}
{% macro cellhead(c, colspan=0) -%}
    <{{ c.type }} class="{{c.class}}" {{ c.attributes|join(" ") }} colspan={{ colspan }}>{{c.value}}</{{ c.type }}>
{%- endmacro %}
{%- block head_tr scoped %}
    <tr> 
            {{ cellhead(r[0]) }}{{ cellhead(r[2])}}{{ cellhead(r[3])}}
    </tr>
    <tr> {{ cellhead(r[1],4)}} </tr>
    <tr> {{ cellhead(r[4],4)}} </tr>
    {%- endblock head_tr %}
{%- block tr scoped %}
    <tr class="dialoghead">
        {{ cell(r[0], 'dialogId') }}{{ cell(r[2], 'quality_alice')}}{{ cell(r[3], 'quality_bob')}}
    </tr>
    <tr>{{ cell(r[1], 'context', 4) }}</tr>
    <tr>{{ cell(r[4], 'text', 4) }}</tr>
{%- endblock tr %}