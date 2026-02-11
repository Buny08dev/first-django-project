from django import template
from django.utils.http import urlencode
from pprint import pprint

register = template.Library()

category={
    "news":{
        "title":"News",
        "url":"news"
    },
    "about":{
        "title":"About",
        "url":"about"
    },
    "test":{
        "title":"Test",
        'url':'test'
    },
    "url":'home'
}

@register.simple_tag()
def workk():
    return category


@register.simple_tag(takes_context=True)
def change_page_filter(context,**kwargs):

    # print(context['request'].GET)

    query=context['request'].GET.dict()
    
    # print("\n",query,"\n",kwargs)
    
    query.update(kwargs)
    
    return urlencode(query)