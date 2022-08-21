from django.shortcuts import render
from AppMVT.models import familiar,familiar1,familiar2,familiar3,familiar4
from django.http import HttpResponse
from datetime import datetime


def familiar(request,edad):
    datos_familiar = familiar(nombre= "Maria", apellido="Vargas" , email= "mv@gmail.com" ,empleado=True)
    anio = datetime.now().year
    numero = int(edad)
    nacimiento =  anio - numero
    return HttpResponse(F"su año de nacimiento es: {nacimiento}")
    datos_familiar.save()
    contexto = {
         'familiar':datos_familiar

      }
    return render(request,"Template.html",contexto)



def familiar1(request,edad):
    datos_familiar1 = familiar1(nombre= "Avril", apellido="Baudes" , email="Avril@gmail.com" , empleado=False)
    anio = datetime.now().year 
    numero = int(edad)
    nacimiento =  anio - numero
    return HttpResponse(F"su año de nacimiento es: {nacimiento}")
    datos_familiar1.save()
    contexto = {
         'familiar1':datos_familiar1

      }
    return render(request,"Template.html",contexto)  




def familiar2(request,edad):
    datos_familiar2 = familiar2(nombre= "Juan", apellido="Dagostino" , email="Juandag@gmail.com" ,empleado=True )
    anio = datetime.now().year 
    numero = int(edad)
    nacimiento =  anio - numero
    return HttpResponse(F"su año de nacimiento es: {nacimiento}")
    datos_familiar2.save()
    contexto = {
         'familiar':datos_familiar2

      }
    return render(request,"Template.html",contexto)




def familiar3(request,edad):
    datos_familiar3 = familiar3(nombre= "Fernando", apellido="Montero" , email="fermontero@gmail.com" ,empleado=False)
    anio = datetime.now().year
    numero = int(edad)
    nacimiento =  anio - numero
    return HttpResponse(F"su año de nacimiento es: {nacimiento}")
    datos_familiar3.save()
    contexto = {
         'familiar':datos_familiar3

      }
    return render(request,"Template.html",contexto)



def familiar4(request,edad):
    datos_familiar4 = familiar4(nombre= "Matias", apellido="Baudes" , email="Riplik1988@gmail.com",empleado=True )
    anio = datetime.now().year
    numero = int(edad)
    nacimiento =  anio - numero
    return HttpResponse(F"su año de nacimiento es: {nacimiento}")
    datos_familiar4.save()
    contexto = {
         'familiar':datos_familiar4

      }
    return render(request,"Template.html",contexto)