from django.shortcuts import render
from .models import WaterBottle 
from .models import Supplier 
from .models import Account 

# Create your views here.
def base(request):
    return render(request, 'MyInventoryApp/base.html')

def supplier(request):
    Supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/supplier.html', {'suppliers':Supplier_objects})

def waterbottle(request):
    WaterBottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/waterbottle.html', {'wbs':WaterBottle_objects})

# i think we can delete addwb (?)
def addwb(request): 
    WaterBottle_objects = WaterBottle.objects.all() 
    return render(request, 'MyInventoryApp/addwb.html', {'wbs':WaterBottle_objects})

def view_supplier(request):
    return render(request, 'MyInventoryApp/view_supplier.html')

def view_bottles(request):
    WaterBottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'wbs':WaterBottle_objects})

def add_bottle(request, pk):
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

        return redirect('view_supplier') 

    return render(request, 'MyInventoryApp/add_bottle.html', {
        'suppliers': suppliers,
        'pk': pk
    })
    
def manage_account(request, pk):
    d = get_object_or_404(Account, pk=pk)
    return render(request, 'MyInventoryApp/manage_account.html', {'d': d})

def change_password(request, pk):
    d = get_object_or_404(Account, pk=pk)

    if request.method == "POST":
        current = request.POST.get('current_password')
        new = request.POST.get('new_password')
        confirm = request.POST.get('confirm_password')

        if current != d.password:
            return render(request, 'MyInventoryApp/change_password.html', {
                'd': d,
                'error': 'Incorrect current password'
            })

        if new != confirm:
            return render(request, 'MyInventoryApp/change_password.html', {
                'd': d,
                'error': 'Passwords do not match'
            })

        d.password = new
        d.save()

        return redirect('manage_account', pk=d.pk)

    return render(request, 'MyInventoryApp/change_password.html', {'d': d})

def delete_account(request, pk):
    d = get_object_or_404(Account, pk=pk)
    d.delete()
    return redirect('login') 



