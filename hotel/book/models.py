from django.db import models
from django.contrib.auth.models import AbstractUser
import random

def random_price():
    return random.randint(800,2000)

class User(AbstractUser):
    user_id = models.IntegerField(default=0)
    phone = models.IntegerField(default=None, blank=True, null=True)
    avatar = models.CharField(default=None ,max_length=64, blank=True, null=True)
    pass


class Category(models.Model):
    category_id = models.IntegerField(default=None)
    Category_name=models.CharField(default=None, max_length=64)


class Hotel(models.Model):
    city = models.CharField(default=None, max_length=64)
    name = models.CharField(default=None, max_length=64)

    address = models.CharField(default=None, max_length=64)

    overview = models.CharField(default=None, max_length=500)
    highlight = models.CharField(default=None, max_length=64)

    room_types = models.CharField(default=None, max_length=64, )
    rating = models.CharField(default=None, max_length=64)

    price = models.FloatField(default=random_price)
    imgurls = models.TextField(default=None, max_length=600)



    def __str__(self):
        return f"{self.city}"


class Rooms(models.Model):
    title=models.CharField(default=None, max_length=64)
    room_type=models.CharField(default=None, max_length=64)
    room_id = models.ForeignKey( Category,related_name='rooms',on_delete=models.CASCADE)
class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="booking", on_delete=models.CASCADE)
    tracking_id = models.CharField(default='000', max_length=64)

    first_name = models.CharField(default=None, max_length=64)
    last_name = models.CharField(default=None, max_length=64)
    email = models.CharField(default=None, max_length=64)
    phone = models.CharField(default=None, max_length=64)

    room = models.IntegerField(default=1)
    adult = models.IntegerField(default=1)
    child = models.IntegerField(default=0)

    checkin_date = models.CharField(default=None , max_length=64)
    checkout_date = models.CharField(default=None, max_length=64)
    booking_date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=64, default=None, null=False)

    user = models.ForeignKey(User, related_name="booking", on_delete=models.SET_NULL, default=None, null=True, blank=True)

    def __str__(self):
        return self.tracking_id

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions',
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)
    room_id = models.ForeignKey(Booking,
                                    on_delete=models.CASCADE, default=1)
    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class Payments(models.Model):
    customer_id = models.ForeignKey(User,related_name='customer_id',
                                on_delete=models.CASCADE, default=1)
    paymet_date=models.CharField(default=None , max_length=64)




class Rooms(models.Model):
    title=models.CharField(default=None, max_length=64)
    room_type=models.CharField(default=None, max_length=64)
    room_id = models.ForeignKey( Category,related_name='rooms',on_delete=models.CASCADE)


class Archive(models.Model):
        hotel = models.ForeignKey(Hotel, related_name="archive", on_delete=models.CASCADE)
        tracking_id = models.CharField(default='000', max_length=64)
        first_name = models.CharField(default=None, max_length=64)
        last_name = models.CharField(default=None, max_length=64)
        email = models.CharField(default=None, max_length=64)
        phone = models.CharField(default=None, max_length=64)
        # room = models.ForeignKey(Category, on_delete=models.CASCADE)
        room = models.IntegerField(default=1)
        adult = models.IntegerField(default=1)
        child = models.IntegerField(default=0)

        checkin_date = models.CharField(default=None, max_length=64)
        checkout_date = models.CharField(default=None, max_length=64)
        booking_date = models.DateTimeField(auto_now_add=True)
        price = models.CharField(max_length=64, default=None, null=False)

        user = models.ForeignKey(User, related_name="archive", on_delete=models.SET_NULL, default=None, null=True,
                                 blank=True)

class UserArchive(models.Model):
    user_id = models.IntegerField(default=0)
    username=models.CharField(default=None, max_length=64)
    first_name=models.CharField(default=None, max_length=64)
    last_name=models.CharField(default=None, max_length=64)
    phone=models.CharField(default=None, max_length=64)



