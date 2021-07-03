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
    return render(request, 'practice_project/view_proc.html', {'model_fields': model_fields, 'dataset': dataset})

def view_video(request):
    model_fields = [field.name for field in Videocard._meta.get_fields() if field.name != 'order']
    dataset = Videocard.objects.all()
    return render(request, 'practice_project/view_video.html', {'model_fields': model_fields, 'dataset': dataset})

def view_mother(request):
    model_fields = [field.name for field in Motherboard._meta.get_fields() if field.name != 'order']
    dataset = Motherboard.objects.all()
    return render(request, 'practice_project/view_mother.html', {'dataset': dataset})

def view_order(request):
    model_fields = [field.name for field in Order._meta.get_fields()]
    dataset = Order.objects.all()
    return render(request, 'practice_project/view_order.html', {'dataset': dataset})

def view_client(request):
    model_fields = [field.name for field in Client._meta.get_fields() if field.name != 'order']
    dataset = Client.objects.all()
    return render(request, 'practice_project/view_client.html', {'dataset': dataset})    

def proc_detail_view(request, id):
    try:
        # Получаем процессор по-определенному id
        data = Processor.objects.post(id=id)
    except Processor.DoesNotExist:
        raise Http404('Такого процессора не существует')
 
    return render(request, 'practice_project/proc_detail_view.html', {'data': data})

def change_delete(request):
    return render(request, 'practice_project/change_delete.html')

def page_delete_proc(request):
    return render(request, 'practice_project/delete_proc.html')

def delete_proc(request, id):
    try:
        proc = Processor.objects.get(id=id)
        proc.delete()
        return HttpResponseRedirect("'practice_project/view_proc.html'")
    except Processor.DoesNotExist:
        return HttpResponseNotFound("<h2>Процессор не найден</h2>")

def delete_video(request, id):
    try:
        video = Videocard.objects.get(id=id)
        video.delete()
        return render(request, 'practice_project/view_video.html')
    except Processor.DoesNotExist:
        return HttpResponseNotFound("<h2>Видеокарта не найдена</h2>")

def delete_mother(request, id):
    try:
        mother = Motherboard.objects.get(id=id)
        mother.delete()
        return render(request, 'practice_project/view_mother.html')
    except Motherboard.DoesNotExist:
        return HttpResponseNotFound("<h2>Материнская плата не найдена</h2>")

def delete_client(request, id):
    try:
        client = Client.objects.get(id=id)
        client.delete()
        return render(request, 'practice_project/view_client.html')
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")

def delete_order(request, id):
    try:
        order = Order.objects.get(id=id)
        order.delete()
        return render(request, 'practice_project/view_order.html')
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
            return render(request, "practice_project/view_proc.html")
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
            return render(request, "practice_project/view_video.html")
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
            return render(request, "practice_project/view_mother.html")
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
            return render(request, "practice_project/view_client.html")
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
            return render(request, "practice_project/view_order.html")
        else:
            return render(request, "practice_project/update_order.html", {"order": order})
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Заказ не найден</h2>")