from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product, ContactInfo, Category


def home(request):
    latest_products = Product.objects.order_by("-created_at")[:5]
    all_products = Product.objects.all()

    paginator = Paginator(all_products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "latest_products": latest_products,
        "page_obj": page_obj,
        "page_title": "Skystore",
    }

    return render(request, "home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"<h2>Спасибо, {name}, за сообщение! Мы свяжемся с вами в ближайшее время по телефону {phone}.</h2>"
        )

    contact_info = ContactInfo.objects.first()
    context = {"contact_info": contact_info, "page_title": "Контакты"}

    return render(request, "contacts.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {"product": product, "page_title": product.name}
    return render(request, "product_detail.html", context)


def add_product(request):

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        picture = request.FILES.get("picture")
        category_name = request.POST.get("category")
        price = request.POST.get("price")

        category, created = Category.objects.get_or_create(name=category_name)

        product = Product(
            name=name,
            description=description,
            picture=picture,
            category=category,
            price=price,
        )
        product.save()

        return HttpResponse(
            f"<h2>Продукт {name} успешно добавлен! Категория: {category_name} (создана: {created})</h2>"
        )

    return render(request, "add_product.html", {"page_title": "Добавить продукт"})
