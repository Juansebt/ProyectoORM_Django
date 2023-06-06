from django.shortcuts import render,HttpResponse
from appORM.models import *
from django.http import JsonResponse
from django.db.models import Q,Sum, Max, Count, Avg
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from django.conf import settings

# Create your views here.
#consultas a realizar
#1. Cantidad de productos vendidos por Categoria

# def consulta(request):
#     resultado = Categoria.objects.all().values()
#     print(resultado)
#     return HttpResponse(resultado)

#2. Valor total de venta por producto
#3. Valor total de Venta por Categoria
#4. Promedio de Ventas por mes
#5. Máximo valor de una venta
#6. Minimo valor de una venta
#7. Cantidad mayor de un producto vendido

def grafica1(request):
    meses = np.array(["Enero","Febrero","Marzo"])
    ventas = np.array([1,2,3])
    
    plt.title("Ventas primer semestre")
    plt.xlabel("Meses")
    plt.ylabel("Ventas")
    
    plt.bar(meses, ventas)
    
    rutaImagen = os.path.join(settings.MEDIA_ROOT+"\\"+"grafica1.png")
    
    plt.savefig(rutaImagen)
    
    return render(request,"graficas1.html")

def grafica2(request):
    miMes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
    
    consulta = DetalleVenta.objects.values('detVenta__venFecha__month').annotate(totalVentaMes = Sum('detValorDetalle'))    
    print(consulta)
    Xmeses = []
    Yventas = []
    
    for datos in consulta:
        mes = datos['detVenta__venFecha__month']
        Xmeses.append(miMes[mes-1])
        Yventas.append(datos['totalVentaMes'])
        
    plt.title("Ventas totales por mes")
    plt.xlabel("Meses")
    plt.ylabel("Ventas")
    
    plt.bar(Xmeses, Yventas)
    
    fotoRoot = os.path.join(settings.MEDIA_ROOT+"\\"+"grafica2.png")
    
    plt.savefig(fotoRoot)
    
    return render(request,"grafica2.html")

# def grafica3(request):
    
#     consulta = DetalleVenta.objects.values('detProducto').annotate(TotalVentaProducto=Sum('detValorDetalle')) 
    
#     ventas = []
    
#     for datos in consulta:
#         fecha = datos['detVenta__venFecha']
#         ventas.append(datos['TotalVentaDia'])
        
def grafica3(request):
    days = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
    
    consulta = DetalleVenta.objects.values('detVenta__venFecha__week_day').annotate(TotalVentaDia=Sum('detValorDetalle'))
    print(consulta)
    
    XDia = []
    YVentas = []
    
    for datos in consulta:
        dia = datos['detVenta__venFecha__week_day']
        XDia.append(days[dia-1])
        YVentas.append(datos['TotalVentaDia'])
        
    plt.subplot(2, 1, 1)
    plt.pie(YVentas, labels=XDia, autopct="%0.1f %%")
    plt.title("Ventas por día semana")
    
    #----------------------------------------------------------
    consulta = DetalleVenta.objects.values('detProducto__proCategoria').annotate(TotalVentaCategoria=Sum('detValorDetalle'))
    print(consulta)
    
    ventas = []
    categorias = []
    
    for cat in consulta:
        categoria = Categoria.objects.get(pk=cat['detProducto__proCategoria'])
        categorias.append(categoria.catNombre)
        ventas.append(cat['TotalVentaCategoria'])
        
    plt.subplot(2, 1, 2)
    plt.bar(categorias,ventas)
    plt.title("Ventas por categoria")
    plt.xlabel("categorias")
    plt.ylabel("ventas")
    
    rutaImagen = os.path.join(settings.MEDIA_ROOT+"\\"+"grafica3.png")
    
    plt.savefig(rutaImagen)
    
    return render(request,"grafica3.html")

def graficaGoogleExample(request):
    return render(request,"graficaGoogle.html")

def graficaGoogle1(request):
    
    ventasProducto = DetalleVenta.objects.values('detProducto').annotate(TotalVentaProdcutos=Sum('detValorDetalle'))
    
    listaDatos = []
    listaDatos.append(['Producto','ValorVenta']) #Encabezado
    
    for ventaProduct in ventasProducto:
        producto = Producto.objects.get(pk=ventaProduct['detProducto']).proNombre
        valorVenta = ventaProduct['TotalVentaProdcutos']
        listaDatos.append([producto,valorVenta])
        
    retorno = {"datos":listaDatos}
    
    return JsonResponse(retorno)

def vistaGraficaGoogle1(request):
    return render(request,'graficaGoogle1.html')