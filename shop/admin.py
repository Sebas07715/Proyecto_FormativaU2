from django.contrib import admin
from shop.models import Cliente, Producto
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'email', 'direccion', 'saldo')
    list_filter = ('nombre', 'rut', 'email')
    search_fields = ('nombre', 'rut', 'email')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('articulo', 'precio', 'stock', 'fecha', 'cliente')
    list_filter = ('articulo', 'precio', 'cliente')
    search_fields = ('articulo', 'precio')

