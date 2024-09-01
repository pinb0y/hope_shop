from django import template


register = template.Library()


@register.filter
def make_image_link(data):
    if data:
        return f"/media/{data}"
    return "#"


@register.filter
def cut_100_chars(description):
    return description[:100]
