from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField()
    

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField()
    

    def __str__(self):
        return self.name


class ProdBadge(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    img = models.URLField()
    img2 = models.URLField(null=True, blank=True)
    img3 = models.URLField(null=True, blank=True)
    img4 = models.URLField(null=True, blank=True)
    discount  = models.IntegerField(null=True, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sub_cat = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    badge = models.ForeignKey(ProdBadge, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

    def __str__(self):
        return self.name