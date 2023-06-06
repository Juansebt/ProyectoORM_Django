from django.db import models

# Create your models here.
   
class Categoria(models.Model):
    catNombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self)->str:
        return self.catNombre

class Producto(models.Model):
    proCodigo = models.IntegerField(unique=True)
    proNombre = models.CharField(max_length=50)    
    proPrecio = models.IntegerField()
    proCategoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
   

    def __str__(self)->str:
        return f'{self.proCodigo}->{self.proNombre}'
    
class Venta(models.Model):
    venFecha = models.DateField()
    venCliente = models.CharField(max_length=100)  
    venDireccion = models.CharField(max_length=100)

    def __str__(self)->str:
        return f'{self.venCliente}->{self.venFecha}'
    
class DetalleVenta(models.Model):
    detVenta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    detProducto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    detCantidad = models.IntegerField()
    detValorDetalle = models.IntegerField()
    
    def __str__(self)->str:
        return f'{self.detProducto}->{self.detCantidad}'

    def calcularValorDetalle(self):
        self.detValorDetalle = self.detProducto.proPrecio*self.detCantidad