from django.shortcuts import render
from .models import WaterBottle 
from .models import Supplier 
from .models import Account 
from django.shortcuts import render, redirect, get_object_or_404

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

def view_supplier(request):
    return render(request, 'MyInventoryApp/view_supplier.html')

def view_bottles(request):
    WaterBottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'wbs':WaterBottle_objects})

def add_bottle(request):
    suppliers = Supplier.objects.all()

    if request.method == "POST":
        sku = request.POST.get('sku')
        brand = request.POST.get('brand')
        cost = request.POST.get('cost')
        size = request.POST.get('size')
        mouth_size = request.POST.get('mouth_size')
        color = request.POST.get('color')
        supplier_id = request.POST.get('supplier')
        qty = request.POST.get('qty')

        WaterBottle.objects.create(
            sku=sku,
            brand=brand,
            cost=cost,
            size=size,
            mouth_size=mouth_size,
            color=color,
            supplied_by_id=supplier_id,   
            current_quantity=qty
        )

        return redirect('waterbottle')  

    return render(request, 'MyInventoryApp/add_bottle.html', {
        'suppliers': suppliers
    })

def manage_account(request, pk):
    d = get_object_or_404(Account, pk=pk)
    return render(request, 'MyInventoryApp/manage_account.html', {'d': d})

def change_password(request, pk):
    d = get_object_or_404(Account, pk=pk)

    if request.method == "POST":
        current_pass = request.POST.get('current_password')
        new_pass = request.POST.get('new_password')
        confirm_pass = request.POST.get('confirm_password')

        if current_pass != d.password:
            return render(request, 'MyInventoryApp/change_password.html', {
                'd': d,
                'error': 'Incorrect current password'
            })

        if new_pass != confirm_pass:
            return render(request, 'MyInventoryApp/change_password.html', {
                'd': d,
                'error': 'Passwords do not match'
            })

        d.password = new_pass
        d.save()

        return redirect('manage_account', pk=d.pk)

    return render(request, 'MyInventoryApp/change_password.html', {'d': d})

def delete_account(request, pk):
    d = get_object_or_404(Account, pk=pk)
    d.delete()
    return redirect('login')

