#from django.shortcuts import render

# Create your views here.
#def index1(request):
    #return render(request, 'index1.html')

# User login form in Payment.html
#def payment(request): 
    #if request.method=='POST':
    #   username=request.POST.get('username')
    #  pass1=request.POST.get('pass')
    # user=authenticate(request,username=username,password=pass1)
    #return render(request,'payment.html')



from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Member, Order, Stock
from django import forms

# Mock data for products
products = {
    "IKAN SIAKAP MERAH": {"price": 10.0, "image": "ikan_2.jpg"},
    "IKAN KEMBONG": {"price": 8.0, "image": "kembong.jpg"},
    "IKAN PARI": {"price": 12.0, "image": "pari.png"},
    "UDANG MERAH": {"price": 15.0, "image": "udang_1.jpg"},
    "UDANG": {"price": 13.0, "image": "udang_2.jpg"},
    "IKAN PATIN": {"price": 11.0, "image": "patin_1.jpg"},
    "IKAN TALAPIA": {"price": 9.0, "image": "ikan_3.jpg"},
    "IKAN HARUAN": {"price": 14.0, "image": "haruan.jpg"},
    "IKAN TOMAN": {"price": 16.0, "image": "toman.jpeg"},
}

cart = {}

def admin_dashboard(request):
    orders = Order.objects.all()  
    stocks = Stock.objects.all()  
    context = {
        'orders': orders,
        'stocks': stocks,
    }
    return render(request, 'members/adminpg.html', context)

def StockForm(request):
    class StockForm(forms.ModelForm):
        class Meta:
            model = Stock
            fields = ['item', 'in_stock', 'out_stock', 'date']

    form = StockForm()
    return render(request, 'adminpg.html', {'form': form})

def add_stock(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    return render(request, 'addstock.html', {'form': form})

@csrf_exempt
def delete_stock(request, stock_id):
    try:
        stock = Stock.objects.get(id=stock_id)
        stock.delete()
        return JsonResponse({'message': 'Stock deleted successfully'}, status=200)
    except Stock.DoesNotExist:
        return HttpResponseNotFound('Stock not found')

def create_order(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        date = request.POST.get('date')
        product = request.POST.get('product')
        status = request.POST.get('status')
        Order.objects.create(user=user, date=date, product=product, status=status)
        return redirect('admin_dashboard')
    return render(request, 'addorder.html')


def delete_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        return JsonResponse({'message': 'Order deleted successfully'}, status=200)
    except Order.DoesNotExist:
        return HttpResponseNotFound('Order not found')






def home(request):
    latest = Member.objects.filter(is_latest=True)
    bestseller = Member.objects.filter(is_bestseller=True)
    special = Member.objects.filter(is_special=True)
    return render(request, 'members/index1.html', {
        'latest': latest,
        'bestseller': bestseller,
        'special': special
    })

def cart_view(request):
    context = {
        "cart": cart,
        "total": sum(item["price"] * quantity for item, quantity in cart.items())
    }
    return render(request, 'cart.html', context)

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        if product_name in products:
            if product_name in cart:
                cart[product_name] += 1
            else:
                cart[product_name] = 1
            return JsonResponse({"status": "success", "cart_count": sum(cart.values())})
    return JsonResponse({"status": "fail"})

def contact_view(request):
    return render(request, 'contact.html')

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Perform login logic here
        return redirect(reverse('home'))
    return render(request, 'admin_login.html')


def fresh_fish_view(request):
    return render(request, 'freshfish.html') 

def fresh_shellfish_view(request):
    return render(request, 'freshshellfish.html') 

def frozen_shellfish_view(request):
    return render(request, 'frozenshellfish.html') 

def payment(request):
    if request.method == 'POST':
        # Handle payment receipt upload
        payment_receipt = request.FILES.get('payment_receipt')
        
        # Process payment receipt here (e.g., save it to a model, verify payment, etc.)
        
        # Dummy response for demonstration
        if payment_receipt:
            # Process the payment receipt (save to database, validate, etc.)
            # Replace the dummy success check with your actual payment validation logic
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    
    # Handle GET request or other methods
    return render(request, 'login.html')

def admin_page_view(request):
    return render(request, 'members/adminpg.html') 

def add_order(request):
    return render(request, 'addorder.html')

def add_stock(request):
    return render(request, 'addstock.html')

