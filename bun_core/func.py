from bun_core.models import Products
from django.contrib.postgres.search import SearchVector,SearchRank,SearchQuery,SearchHeadline

def search_func(qq:Products,q):

    query=SearchQuery(q)
    vector=SearchVector('name','description')

    # qq=qq.annotate(search=SearchVector('name','description')).filter(q)
    qq=qq.annotate(rank=SearchRank(vector,query)).exclude(rank__exact=0).order_by('-rank')

    qq = qq.annotate(headline=SearchHeadline('name',query,start_sel="<span style='background-color: yellow;'>",stop_sel="</span>",))
    qq = qq.annotate(bodyline=SearchHeadline('description',query,start_sel="<span style='background-color: yellow;'>",stop_sel="</span>",))
    # print(qq[0].headline)
    return qq