from django.contrib import admin
from .models import StoreDetails,ProductDetails,SalesDetails,FilterDate,StockDetails,profilemodel,SK_Bills

#================Admin=========>
from .models import adminregi,SaleFilter
#<==============================

class StoreDetailsAdmin(admin.ModelAdmin):
    list_display = ['StoreName','email','password']

admin.site.register(StoreDetails,StoreDetailsAdmin)
admin.site.register(ProductDetails)
admin.site.register(SalesDetails)
admin.site.register(FilterDate)
admin.site.register(SaleFilter)
admin.site.register(StockDetails)
admin.site.register(profilemodel)

#=================Admin===========>
admin.site.register(adminregi)
admin.site.register(SK_Bills)