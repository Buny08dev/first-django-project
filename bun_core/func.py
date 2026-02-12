from bun_core.models import Products
from django.contrib.postgres.search import SearchVector,SearchRank,SearchQuery


def search_func(qq:Products,q):

    query=SearchQuery(q)
    vector=SearchVector('name','description')

    # qq=qq.annotate(search=SearchVector('name','description')).filter(q)
    qq=qq.annotate(rank=SearchRank(vector,query)).exclude(rank__exact=0).order_by('-rank')

    return qq