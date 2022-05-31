from django.contrib import admin

# Register your models here.
from .models import User,Hotel,Booking, Transaction,Category, Rooms, Archive, UserArchive

class UserAdmin(admin.ModelAdmin):
    list_display = ('phone',)
admin.site.register(User, UserAdmin)


class HotelAdmin(admin.ModelAdmin):
    list_display = ('city','name', 'address','overview', 'highlight', 'room_types', 'rating', 'price', 'imgurls', )
admin.site.register(Hotel, HotelAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('hotel','tracking_id', 'first_name','last_name', 'email', 'phone', 'adult', 'child', 'checkin_date', 'checkout_date', 'booking_date', 'price', 'user')
admin.site.register(Booking, BookingAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('made_by','made_on', 'amount','order_id', 'checksum')
admin.site.register(Transaction, TransactionAdmin)


# class PaymentsAdmin(admin.ModelAdmin):
#     list_display = ('customer_id', 'payment_date')
# admin.site.register(Payments, PaymentsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'Category_name')
admin.site.register(Category, CategoryAdmin)


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('title', 'room_id')
admin.site.register(Rooms, RoomsAdmin)

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','phone','room','adult','child', 'checkin_date', 'checkout_date','booking_date','price','hotel_id', 'user_id')
admin.site.register(Archive, ArchiveAdmin)

class UserArchiveAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'first_name', 'last_name','phone')
admin.site.register(UserArchive, UserArchiveAdmin)

