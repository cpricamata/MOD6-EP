from django.shortcuts import render
from .models import WaterBottle 
from .models import Supplier 

# Create your views here.
def base(request):
    return render(request, 'MyInventoryApp/base.html')

def supplier(request):
    Supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/supplier.html', {'suppliers':Supplier_objects})

def waterbottle(request):
    WaterBottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/waterbottle.html', {'wbs':WaterBottle_objects})

def addwb(request):
    WaterBottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/addwb.html', {'wbs':WaterBottle_objects})

def view_supplier(request):
    return render(request, 'MyInventoryApp/view_supplier.html')

def view_bottles(request):
    WaterBottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'wbs':WaterBottle_objects})

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')


