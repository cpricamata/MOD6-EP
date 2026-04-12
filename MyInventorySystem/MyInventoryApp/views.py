from django.shortcuts import render
from .models import WaterBottle 
from .models import Supplier 

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Account.objects.filter(username=username, password=password).first()

        if user:
            return redirect('base')
        else:
            return render(request, 'MyInventoryApp/login.html', {
                'error': 'Invalid login'
            })

    return render(request, 'MyInventoryApp/login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Account.objects.filter(username=username).exists():
            return render(request, 'MyInventoryApp/signup.html', {
                'error': 'Username already exists'
            })

        Account.objects.create(username=username, password=password)
        return redirect('login')

    return render(request, 'MyInventoryApp/signup.html')

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



