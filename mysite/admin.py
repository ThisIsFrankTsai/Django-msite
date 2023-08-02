from django.contrib import admin
from mysite.models import NewTable,Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin) :
    list_display=('name','price','qty')


admin.site.register(NewTable)
admin.site.register(Product,ProductAdmin)