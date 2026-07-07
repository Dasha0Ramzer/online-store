from itertools import product

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView

from catalog.models import Product, ContactInfo, Category


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_products = Product.objects.all()
        paginator = Paginator(all_products, 2)
        page_number = self.request.GET.get("page")
        context["page_obj"] = paginator.get_page(page_number)

        context["page_title"] = "Skystore"
        return context


class ContactsView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"<h2>Спасибо, {name}, за сообщение! Мы свяжемся с вами в ближайшее время по телефону {phone}.<h2>"
        )

    def get(self, request, *args, **kwargs):
        contact_info = ContactInfo.objects.first()
        context = {"contact_info": contact_info, "page_title": "Контакты"}
        return render(request, "contacts.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.name
        return context


class AddProductView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "add_product.html", {"page_title": "Добавить продукт"})

    def post(self, request, *args, **kwargs):
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
