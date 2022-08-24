from django.shortcuts import render
from email import message
from django.shortcuts import render
from App_MVT.models import Familiar
from datetime import datetime


def familiar(request,edad):
    familiar1 = Familiar(nombre= "Maria", apellido="Vargas" , email= "mv@gmail.com" ,empleado=True, edad=edad,fecha="1963-4-15")
    familiar2 = Familiar(nombre= "Juan", apellido="Dagostino" , email= "jd@gmail.com" ,empleado=False, edad=edad,fecha="1999-2-22")
    familiar3 = Familiar(nombre= "Marcos", apellido="Rodriguez" , email= "mr@gmail.com" ,empleado=True, edad=edad,fecha="1988-7-18")
    
    
    familiar1.save()
    contexto = {
         'familiar1':familiar1,
         'familiar2':familiar2,
         'familiar3':familiar2,

      }
    return render(request,"Template.html",contexto)