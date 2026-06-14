from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, ContactInfo


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"<h2>Спасибо, {name}, за сообщение! Мы свяжемся с вами в ближайшее время по телефону {phone}.</h2>"
        )

    contact_info = (
        ContactInfo.objects.first()
    )  # Предполагается, что существует одна запись

    return render(request, "contacts.html", {"contact_info": contact_info})


def home_view(request):
    latest_products = Product.objects.order_by("-created_at")[:5]

    for product in latest_products:
        print(product)

    return render(request, "home.html", {"latest_products": latest_products})
