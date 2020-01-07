from django.contrib import admin
from .models import User, Store, Coupon, UserCoupon

# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'hp',
        'created_at',
        'updated_at'
    )
    
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'tel',
        'created_at',
        'updated_at'
    )
    
@admin.register(Coupon)   
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'detail',
        'count',
        'due',
        'img',
        'store',
        'created_at',
        'updated_at'
    )
    
@admin.register(UserCoupon)   
class UserCouponAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'coupon',
        'created_at',
        'updated_at'
    )
    