from django.urls import path,include
from bun_core.views import (test, create_,MainView,AboutView,ProductView,
NewsView,DeleteProductView,UpdateProductView,
ProductsViewSet
)
from rest_framework import routers

router=routers.SimpleRouter()
router.register(r'api',ProductsViewSet,basename='api')


urlpatterns = [
    path("",MainView.as_view()  ,name="home"),
    # Base urls
    path("news/", NewsView.as_view(), name="news"),
    path("about/",AboutView.as_view(),name="about"),
    path("test/",test,name="test"),
    # Create, Update, Read and Delete (CRUD) urls
    path("create/",create_, name="create"),
    path('delete/<slug:slug>/',DeleteProductView.as_view(),name="delete"),
    path('update/<slug:slug>/',UpdateProductView.as_view(),name='update'),
    # decorative urls
    path("news/<slug:category_slug>/<slug:product_slug>",ProductView.as_view(), name="product_slug"),
    # api
    path('',include(router.urls))
]

