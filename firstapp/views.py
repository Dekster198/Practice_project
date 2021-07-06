from rest_framework import generics, permissions
from django.contrib.auth.models import User
from practice_project import serializers
from .forms import *
from firstapp.models import Processor
from django import http
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    return render(request, 'practice_project/index.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Страница не найдена</h1>')

def change_create(request):
    return render(request, 'practice_project/change_create.html')

def change_rud(request):
    return render(request, 'practice_project/change_rud.html')

def add_proc(request):
    if (request.method == 'POST'):
        form = AddProc(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('add_proc')
    else:
        form = AddProc()
    return render(request, "practice_project/add_proc.html", {"form": form, 'title': 'Добавление процессора'})

def add_video(request):
    if (request.method == 'POST'):
        form = AddVideo(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('add_video')
    else:
        form = AddVideo()
    return render(request, "practice_project/add_video.html", {"form": form, 'title': 'Добавление видеокарты'})

def add_mother(request):
    if (request.method == 'POST'):
        form = AddMother(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('add_mother')
    else:
        form = AddMother()
    return render(request, "practice_project/add_mother.html", {"form": form, 'title': 'Добавление материнской платы'})

def add_client(request):
    if (request.method == 'POST'):
        form = AddClient(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('add_client')
    else:
        form = AddClient()
    return render(request, "practice_project/add_client.html", {"form": form, 'title': 'Добавление клиента'})

def add_order(request):
    if (request.method == 'POST'):
        form = AddOrder(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('add_order')
    else:
        form = AddOrder()
    return render(request, "practice_project/add_order.html", {"form": form, 'title': 'Добавление заказа'})

def view_proc(request):
    model_fields = [field.name for field in Processor._meta.get_fields() if field.name != 'order']
    dataset = Processor.objects.all()
    filter_form = FilterFormProduct(request.GET)
    if(filter_form.is_valid()):
        if(filter_form.cleaned_data['min_price']):
            dataset = dataset.filter(price__gte=filter_form.cleaned_data['min_price'])
        if(filter_form.cleaned_data['max_price']):
            dataset = dataset.filter(price__lte=filter_form.cleaned_data['max_price'])   
        if(filter_form.cleaned_data['ordering']):
            dataset = dataset.order_by(filter_form.cleaned_data['ordering']) 
    return render(request, 'practice_project/view_proc.html', {'model_fields': model_fields, 'dataset': dataset, 'filter_form': filter_form})

def view_video(request):
    model_fields = [field.name for field in Videocard._meta.get_fields() if field.name != 'order']
    dataset = Videocard.objects.all()
    filter_form = FilterFormProduct(request.GET)
    if(filter_form.is_valid()):
        if(filter_form.cleaned_data['min_price']):
            dataset = dataset.filter(price__gte=filter_form.cleaned_data['min_price'])
        if(filter_form.cleaned_data['max_price']):
            dataset = dataset.filter(price__lte=filter_form.cleaned_data['max_price'])   
        if(filter_form.cleaned_data['ordering']):
            dataset = dataset.order_by(filter_form.cleaned_data['ordering']) 
    return render(request, 'practice_project/view_video.html', {'model_fields': model_fields, 'dataset': dataset, 'filter_form': filter_form})

def view_mother(request):
    model_fields = [field.name for field in Motherboard._meta.get_fields() if field.name != 'order']
    dataset = Motherboard.objects.all()
    filter_form = FilterFormProduct(request.GET)
    if(filter_form.is_valid()):
        if(filter_form.cleaned_data['min_price']):
            dataset = dataset.filter(price__gte=filter_form.cleaned_data['min_price'])
        if(filter_form.cleaned_data['max_price']):
            dataset = dataset.filter(price__lte=filter_form.cleaned_data['max_price'])   
        if(filter_form.cleaned_data['ordering']):
            dataset = dataset.order_by(filter_form.cleaned_data['ordering']) 
    return render(request, 'practice_project/view_mother.html', {'dataset': dataset, 'filter_form': filter_form})

def view_order(request):
    model_fields = [field.name for field in Order._meta.get_fields()]
    dataset = Order.objects.all()
    filter_form = FilterFormOrder(request.GET)
    if(filter_form.is_valid()):  
        if(filter_form.cleaned_data['ordering']):
            dataset = dataset.order_by(filter_form.cleaned_data['ordering']) 
    return render(request, 'practice_project/view_order.html', {'dataset': dataset, 'filter_form': filter_form})

def view_client(request):
    model_fields = [field.name for field in Client._meta.get_fields() if field.name != 'order']
    dataset = Client.objects.all()
    filter_form = FilterFormClient(request.GET)
    if(filter_form.is_valid()):  
        if(filter_form.cleaned_data['ordering']):
            dataset = dataset.order_by(filter_form.cleaned_data['ordering']) 
    return render(request, 'practice_project/view_client.html', {'dataset': dataset, 'filter_form': filter_form})    

def change_delete(request):
    return render(request, 'practice_project/change_delete.html')

def delete_proc(request, id):
    try:
        proc = Processor.objects.get(id=id)
        proc.delete()
        return redirect('view_proc')
    except Processor.DoesNotExist:
        return HttpResponseNotFound("<h2>Процессор не найден</h2>")

def delete_video(request, id):
    try:
        video = Videocard.objects.get(id=id)
        video.delete()
        return redirect('view_video')
    except Processor.DoesNotExist:
        return HttpResponseNotFound("<h2>Видеокарта не найдена</h2>")

def delete_mother(request, id):
    try:
        mother = Motherboard.objects.get(id=id)
        mother.delete()
        return redirect('view_mother')
    except Motherboard.DoesNotExist:
        return HttpResponseNotFound("<h2>Материнская плата не найдена</h2>")

def delete_client(request, id):
    try:
        client = Client.objects.get(id=id)
        client.delete()
        return redirect('view_client')
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")

def delete_order(request, id):
    try:
        order = Order.objects.get(id=id)
        order.delete()
        return redirect('view_order')
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Заказ не найден</h2>")

def update_proc(request, id):
    try:
        proc = Processor.objects.get(id=id)
        if request.method == "POST":
            proc.manufacturer = request.POST.get("manufacturer")
            proc.model = request.POST.get("model")
            proc.frequency = request.POST.get("frequency")
            proc.socket = request.POST.get("socket")
            proc.cores = request.POST.get("cores")
            proc.threads = request.POST.get("threads")
            proc.quantity = request.POST.get("quantity")
            proc.price = request.POST.get("price")
            proc.photo = request.POST.get("photo")
            proc.save()
            return redirect('view_proc')
        else:
            return render(request, "practice_project/update_proc.html", {"proc": proc})
    except Processor.DoesNotExist:
        return HttpResponseNotFound("<h2>Процессор не найден</h2>")

def update_video(request, id):
    try:
        video = Videocard.objects.get(id=id)
        if request.method == "POST":
            video.manufacturer = request.POST.get("manufacturer")
            video.model = request.POST.get("model")
            video.memory_type = request.POST.get("memory_type")
            video.memory_size = request.POST.get("memory_size")
            video.quantity = request.POST.get("quantity")
            video.price = request.POST.get("price")
            video.photo = request.POST.get("photo")
            video.save()
            return redirect('view_video')
        else:
            return render(request, "practice_project/update_video.html", {"video": video})
    except Processor.DoesNotExist:
        return HttpResponseNotFound("<h2>Видеокарта не найдена</h2>")

def update_mother(request, id):
    try:
        mother = Motherboard.objects.get(id=id)
        if request.method == "POST":
            mother.manufacturer = request.POST.get("manufacturer")
            mother.model = request.POST.get("model")
            mother.socket = request.POST.get("socket")
            mother.chipset = request.POST.get("chipset")
            mother.memory_slots = request.POST.get("memory_slots")
            mother.max_memory_frequency = request.POST.get("max_memory_frequency")
            mother.quantity = request.POST.get("quantity")
            mother.price = request.POST.get("price")
            mother.photo = request.POST.get("photo")
            mother.save()
            return redirect('view_mother')
        else:
            return render(request, "practice_project/update_mother.html", {"mother": mother})
    except Processor.DoesNotExist:
        return HttpResponseNotFound("<h2>Материнская плата не найдена</h2>")

def update_client(request, id):
    try:
        client = Client.objects.get(id=id)
        if request.method == "POST":
            client.name = request.POST.get("name")
            client.surname = request.POST.get("surname")
            client.patronymic = request.POST.get("patronymic")
            client.phone_number = request.POST.get("phone_number")
            client.city = request.POST.get("city")
            client.street = request.POST.get("street")
            client.house = request.POST.get("house")
            client.flat = request.POST.get("flat")
            client.email = request.POST.get("email")
            client.password = request.POST.get("password")
            client.save()
            return redirect('view_client')
        else:
            return render(request, "practice_project/update_client.html", {"client": client})
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")

def update_order(request, id):
    try:
        order = Order.objects.get(id=id)
        if request.method == "POST":
            order.price = request.POST.get("price")
            order.id_client_id = request.POST.get("id_client_id")
            order.id_proc_id = request.POST.get("id_proc_id")
            order.id_video_id = request.POST.get("id_video_id")
            order.id_mother_id = request.POST.get("id_mother_id")
            order.save()
            return redirect('view_order')
        else:
            return render(request, "practice_project/update_order.html", {"order": order})
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Заказ не найден</h2>")

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

class ProcessorList(generics.ListCreateAPIView):
    queryset = Processor.objects.all()
    serializer_class = serializers.ProcessorSerializer

class ProcessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Processor.objects.all()
    serializer_class = serializers.ProcessorSerializer

class VideocardList(generics.ListCreateAPIView):
    queryset = Videocard.objects.all()
    serializer_class = serializers.VideocardSerializer

class VideocardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videocard.objects.all()
    serializer_class = serializers.VideocardSerializer

class MotherboardList(generics.ListCreateAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = serializers.MotherboardSerializer

class MotherboardDetail(generics.RetrieveAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = serializers.MotherboardSerializer