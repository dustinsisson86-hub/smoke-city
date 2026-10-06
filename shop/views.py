from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Product, FeaturedProduct
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def home(request):
    featured = FeaturedProduct.objects.filter(active=True).first()
    return render(request, 'shop/home.html', {'featured': featured})

def products(request):
    items = Product.objects.all()
    return render(request, 'shop/products.html', {'items': items})

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

class CustomAdminLoginView(LoginView):
    template_name = 'shop/admin_login.html'
    redirect_authenticated_user = True