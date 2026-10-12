from django.contrib import admin
from shop.models import Cliente, Producto
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'rut', 'email', 'direccion', 'Saldo_Cliente')
    list_filter = ('id',)
    search_fields = ('id','nombre', 'rut', 'email')

    def Saldo_Cliente (self, obj):

        return f"${obj.saldo:,}".replace(",", ".")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','articulo', 'Total', 'stock', 'fecha', 'cliente')
    list_filter = ('id', 'fecha','stock')
    search_fields = ('id','articulo', 'precio',)


    def Total (self, obj):

        return f"${obj.precio:,}".replace(",", ".")
