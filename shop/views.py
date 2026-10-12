from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Product, FeaturedProduct
from django.contrib.auth.views import LoginView

# HOME PAGE
def home(request):
    featured = FeaturedProduct.objects.filter(active=True).first()
    return render(request, 'shop/home.html', {'featured': featured})

# PRODUCT LIST PAGE (your main products page)
def products(request):
    items = Product.objects.all()
    return render(request, 'shop/products.html', {'items': items})

# CONTACT PAGE
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()

            send_mail(
                subject=f"New message from {message.name}",
                message=message.message,
                from_email=message.email,
                recipient_list=["youremail@example.com"],  # change this
                fail_silently=False,
            )
            return render(request, 'shop/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'shop/contact.html', {'form': form})

# CUSTOM ADMIN LOGIN
class CustomAdminLoginView(LoginView):
    template_name = 'shop/admin_login.html'
    redirect_authenticated_user = True

# CLICKABLE PRODUCT LIST (for /shop/)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

# PRODUCT DETAIL PAGE (for /shop/product/<pk>/)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})
