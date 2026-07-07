from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from blog.models import Note


class BlogListView(ListView):
    model = Note
    template_name = "note_list.html"

    def get_queryset(self):
        return Note.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_products = self.get_queryset()
        paginator = Paginator(all_products, 10)
        page_number = self.request.GET.get("page")
        context["page_obj"] = paginator.get_page(page_number)
        context["page_title"] = "Блог"
        return context


class BlogCreateView(CreateView):
    model = Note
    fields = ["heading", "content", "preview"]
    template_name = "note_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Написать статью"
        return context


class BlogDetailView(DetailView):
    model = Note
    template_name = "note_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Статья"
        return context


class BlogUpdateView(UpdateView):
    model = Note
    fields = ["heading", "content", "preview"]
    template_name = "note_update.html"

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Редактировать статью"
        return context


class BlogDeleteView(DeleteView):
    model = Note
    template_name = "note_delete.html"
    success_url = "/blog/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Удалить статью"
        return context
