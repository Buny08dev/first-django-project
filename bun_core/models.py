from django.db import models
from django.utils.text import slugify

# Create your models here.

# Categories
class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
           self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

    
    class Meta:
        db_table="Category"
        verbose_name="category"
        verbose_name_plural="categorylar"

# Skidka
class Sale(models.Model):
    name = models.CharField(max_length=150,verbose_name="Skidka nomi")
    percent = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="Skida foizda")
    start_date = models.DateTimeField(verbose_name="Qachon boshlanishi")
    end_date = models.DateTimeField(verbose_name="Qachon tugashi")
    active = models.BooleanField(default=False,verbose_name="Skidka ishlasinmi?")

    def __str__(self):
        return self.name
# Products
class Products(models.Model):
    name=models.CharField(max_length=150,verbose_name="Nomi")
    slug=models.SlugField(max_length=200,verbose_name="Slug")
    description=models.TextField(verbose_name="Product haqida")
    image=models.ImageField(blank=True,null=True,verbose_name="Rasm")
    price=models.DecimalField(max_digits=11,decimal_places=2,verbose_name="Narx")
    quantity=models.PositiveIntegerField(verbose_name="Soni")
    sales=models.ForeignKey(to=Sale, blank=True,null=True,on_delete=models.SET_NULL, related_name="products",verbose_name="Skidka")
    created_time=models.DateField(verbose_name="Vaqt",auto_now_add=True)
    updt_time=models.DateTimeField(verbose_name="Yangilangan vaqti",auto_now=True)

    category=models.ForeignKey(to=Categories,on_delete=models.CASCADE,related_name="products")

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Products.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        return super().save(*args, **kwargs)
    
    def change_price(self):
        if self.sales:
            return round(self.price-(self.price*self.sales.percent)/100,2)
        return self.price

    class Meta:
        db_table="Product"
        verbose_name="product"
        verbose_name_plural="productlar"



# Bunbase
class bunbase(models.Model):
    title=models.CharField(max_length=150,verbose_name="nomi")
    description=models.TextField(blank=True,verbose_name="haqida")
    create_ad=models.DateField(auto_now_add=True)
    image=models.ImageField(blank=True,null=True,verbose_name="rasm")
    time=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True,verbose_name="active")
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table="bunbase"
        verbose_name="bun base"
        verbose_name_plural="bun base"