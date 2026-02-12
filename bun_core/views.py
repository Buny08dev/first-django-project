from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
# from django.http import HttpResponse
from django.views.generic import FormView,ListView,View,DetailView,TemplateView,DeleteView,UpdateView
# from django.core.paginator import Paginator
from django.urls import reverse_lazy
# from django.contrib import messages
#  rest_framework
# from rest_framework.views import APIView
# from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
from rest_framework import viewsets
# bunbase
from bun_core.forms import AddProduct,SearchForm
from bun_core.models import bunbase,Categories,Products
from bun_core.serializers import ProductsApiForm
from bun_core.func import search_func

# bunbase.objects.values("id", "title")

# bunbase.objects.values_list("title", flat=True) only one o`zgaruvchi

# bunbase.objects.count()

# bunbase.objects.bulk_create([
#     bunbase(title="A"),
#     bunbase(title="B"),
# ])  ishlatarman!!


# Create your Apiviews here.
# class ProductApi(APIView):
#     def get(self,request):
#         title=Products.objects.values()
#         print(request.data)
#         return Response({"title":title})


class ProductsViewSet(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductsApiForm
# Create your views here.
class MainView(View):
    def get(self,request):
        return render(request, 'home.html', {"title":"hello world"})

class NewsView(ListView):
    model=Products
    context_object_name="products_"
    template_name="news.html"
    paginate_by=3
    
    def get_queryset(self,*args,**kwargs):
        queryset = super().get_queryset(*args,**kwargs)
        # print("\n",self.request.GET,"\n1"

        form = SearchForm(self.request.GET)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            if len(search.strip())>2 and len(search) > 2:
                queryset=search_func(queryset,search)

        slug=self.request.GET.get("cat_slug")
        if slug:
            queryset=queryset.filter(category__slug=slug)

        pr=self.request.GET.get("default")
        if pr:
            queryset=queryset.all()

        pr_1=self.request.GET.get("on_sale")
        if pr_1:
            queryset=queryset.all().order_by(pr_1)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print("\n",context,"\n")
        context["categories"] = Categories.objects.all()
        context["searchform"] = SearchForm(self.request.GET)
        context["products"]=context['page_obj']

        return context

class ProductView(DetailView):
    model=Products
    context_object_name="product"
    template_name="product_view.html" 
    slug_field="slug"
    slug_url_kwarg="product_slug"

    def get_queryset(self):
        return Products.objects.filter(category__slug=self.kwargs['category_slug'])

class AboutView(TemplateView):
    template_name="about.html"

def create_(request):
    if request.method=="POST":
        print("ishladi")
        form=AddProduct(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news")
    form=AddProduct()
    return render(request, "main.html",{"agree":"yes","form":form})

class UpdateProductView(UpdateView):
    model=Products
    form_class=AddProduct
    template_name="main.html"
    success_url=reverse_lazy('news')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["agree"]="agree"
        return context

class DeleteProductView(DeleteView):
    model=Products    
    success_url=reverse_lazy('news')

# TESTing
def test(request):
    # print(request.GET.get("name"))
    # print(request.GET.get("year"))
    # print(request.GET)
    # pagenation=Paginator(get_list_or_404(Products),2)
    # page_product=pagenation.page(page)
    return render(request,"test.html")

# Created your views here.

# def product_view(request,category_slug,product_slug):
#     prod=Products.objects.filter(category__slug=category_slug,slug=product_slug)
#     return render(request,"product_view.html",{"products":prod})

# def news(request,slug=None):
#     prod=Products.objects.all()
#     cat=Categories.objects.all()
#     if slug:
#         prod=Products.objects.filter(category__slug=slug)
#     return render(request, "news.html",{"products":prod,"categories":cat})

# def delete_(request,id):
#     Products.objects.get(id=id).delete()
#     return redirect("news")

# def update_(request,id):
#     if request.method=="POST":
#         obj=bunbase.objects.get(id=id)
#         obj.title = request.POST.get("title")
#         obj.description = request.POST.get("description")
#         obj.is_active = request.POST.get("is_active")
#         if "image" in request.FILES:
#             obj.image = request.FILES.get("image")
#         obj.save()
#         return redirect("news")
#     return render(request, "main.html",{"agree":"yes"})