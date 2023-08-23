from django.db import models


STATUS_CHOICES = (
    ('pending', 'pending'),
    ('packed', 'packed'),
    ('shipped', 'shipped'),
    ('delivered', 'delivered'),
    ('completed', 'completed'),

    
)


PAYMENT_CHOICES = (
    ('pending', 'pending'),
    ('completed', 'completed'),
)


class Category(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        db_table = 'web_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('-id',)

    def __str__(self):
        return self.name
    

class Size(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        db_table = 'web_size'
        verbose_name = 'size'
        verbose_name_plural = 'sizes'
        ordering = ('-id',)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to="product")
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size)
    is_stock = models.BooleanField(default=True)

    class Meta:
        db_table = 'web_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    moblie = models.IntegerField()
    address = models.TextField()
    pincode = models.CharField(max_length=8)
    qty = models.IntegerField(default=1)
    amount = models.IntegerField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    payment_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'web_order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ('-id',)

    def __str__(self):
        return self.name 
    