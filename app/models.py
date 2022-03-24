from django.db import models
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
    Discount = models.IntegerField()

    def __str__(self):
        return self.Quote



