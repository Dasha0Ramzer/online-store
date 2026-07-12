from itertools import product

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm
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


class AddProductView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, "add_product.html", {"form": form, "page_title": "Добавить продукт"})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return HttpResponse(
                f"<h2>Продукт {product.name} успешно добавлен!</h2>"
            )
        return render(request, "add_product.html", {"form": form, "page_title": "Добавить продукт"})


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_update.html"

    def get_success_url(self):
        return reverse("catalog:product_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Редактировать продукт"
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_delete.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Удалить продукт"
        return context
