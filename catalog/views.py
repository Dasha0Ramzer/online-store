from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        return HttpResponse(f"<h2>Спасибо, {name}, за сообщение! Мы свяжемся с вами в ближайшее время по телефону {phone}.</h2>")

    return render(request, 'contacts.html')

