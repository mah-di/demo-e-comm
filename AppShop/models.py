from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=264, verbose_name='Category title')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'

    

class Product(models.Model):
    image = models.ImageField(upload_to='Products', verbose_name='Product Image')
    name = models.CharField(max_length=264, verbose_name='Product Name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    description = models.TextField(max_length=2000, verbose_name='Prdouct Description')
    preview_text = models.CharField(max_length=400, verbose_name='Short Description')
    regular_price = models.FloatField(verbose_name='Regular Price')
    discounted_price = models.FloatField(verbose_name='Discounted Price')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']