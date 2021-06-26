from django import template

register = template.Library()

def range_filter(value):
    # 1st 500 char retuen korbe.. sathe ... add korbe
    return value[0:500] + "........."

register.filter('range_filter', range_filter)
