from django.db import models
from ckeditor.fields import RichTextField
STATUS=(('active','active'),('','default'))
LABELS=(('special','special'),('','default'))


# Create your models here.
class slider(models.Model):
    DISCOUNT_DEAL = (
        ('HOT DEALS','HOT DEALS'),
        ('New Arraivels','New Arraivels'),
        ('New DEALS','New DEALS'))
    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(choices = DISCOUNT_DEAL,max_length=100)
    SALE = models.IntegerField()
    Brand_Name = models.CharField(max_length=500)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=500)
    Rank = models.IntegerField()
    Status = models.CharField(max_length=300, choices=STATUS, blank=True)

    def __str__(self):
        return self.Brand_Name

class Banner(models.Model):
    Image = models.ImageField(upload_to='media/banner_imgs')
    Discount_Deal = models.CharField(max_length=100)
    Quote= models.CharField(max_length=400)
    Link = models.CharField(max_length=500,null=True)
    Discount = models.IntegerField()

    def __str__(self):
        return self.Quote

class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    main_category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + "--" + self.main_category.name

class Subcategory(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name + "--" + self.category.name + "--" +self.name

class Section(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Product(models.Model):
    total_quantity = models.IntegerField()
    Availability = models.IntegerField()
    featured_image = models.ImageField(upload_to='media/product_imgs')
    Product_name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Discount = models.IntegerField()
    Product_information = RichTextField(blank=True)
    model_Name = models.CharField(max_length=100)
    Categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    Tags = models.CharField(max_length=100)
    Description = RichTextField()
    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Product_name

class Product_Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Image_url = models.CharField(max_length = 200)

class Additional_Information(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)



