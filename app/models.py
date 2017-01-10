from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=30)
    employee_name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.employee_name)

class Menu(models.Model):
    entry = models.CharField(max_length=30)
    price = models.FloatField()
    #date = models.DateTimeField(default=datetime.now, blank=True)
    #employee = models.ForeignKey('auth.User')
    name = models.CharField(max_length=35)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        ordering =('name',)

class Order(models.Model):
    server_id = models.ForeignKey(User)
    time_stamp = models.DateTimeField(auto_now=True)
    total_bill = models.ForeignKey(Menu)
    is_cashed = models.BooleanField(default=False)
    table_number = models.IntegerField()
    is_server = models.CharField(max_length=30)
    is_completed = models.BooleanField(default=False)
    memo_notes = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return self.is_server

    class Meta:
        ordering = ('table_number',)

class Check(models.Model):
    server = models.ForeignKey(User)
    price = models.ManyToManyField(Menu)
    quanity = models.IntegerField()
    check_number = models.ForeignKey(Order)
    is_completed = models.BooleanField(default=False)
    memo_notes = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return str(self.server)

class Menu_Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_image = models.ImageField(upload_to='uploads', blank=True, null=True)
    item_cost = models.DecimalField(max_digits=6, decimal_places=2)
    item_description = models.TextField(max_length=None)
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/uploads/default.png"

    def __str__(self):
        return self.item_name
