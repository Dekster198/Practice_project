from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    city = models.CharField(max_length=25, verbose_name='Город')
    street = models.CharField(max_length=20, verbose_name='Улица')
    house = models.CharField(max_length=5, verbose_name='Дом')
    flat = models.CharField(max_length=5, blank=True, verbose_name='Квартира')
    email = models.CharField(max_length=50, verbose_name='Email')
    password = models.CharField(max_length=50, verbose_name='Пароль')

class Processor(models.Model):
    manufacturer = models.CharField(max_length=15, verbose_name='Производитель')
    model = models.CharField(max_length=25, verbose_name='Модель')
    frequency = models.IntegerField(verbose_name='Частота')
    socket = models.CharField(max_length=15, verbose_name='Сокет')
    cores = models.IntegerField(verbose_name='Количество ядер')
    threads = models.IntegerField(verbose_name='Количество потоков')
    quantity = models.IntegerField('Количество на складе')
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='images/proc/', verbose_name='Изображение процессора')

class Videocard(models.Model):
    manufacturer = models.CharField(max_length=15, verbose_name='Производитель')
    model = models.CharField(max_length=25, verbose_name='Модель')
    memory_type = models.CharField(max_length=6, verbose_name='Тип памяти')
    memory_size = models.IntegerField(verbose_name='Количество памяти')
    quantity = models.IntegerField(verbose_name='Количество на складе')
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='images/video/', verbose_name='Изображение видеокарты')

class Motherboard(models.Model):
    manufacturer = models.CharField(max_length=15, verbose_name='Производитель')
    model = models.CharField(max_length=25, verbose_name='Модель')
    socket = models.CharField(max_length=15, verbose_name='Сокет')
    chipset = models.CharField(max_length=15, verbose_name='Чипсет')
    memory_slots = models.IntegerField(verbose_name='Количетсов слотов памяти')
    max_memory_frequency = models.IntegerField('Максимальная частота памяти')
    quantity = models.IntegerField('Количество на складе')
    price = models.IntegerField('Цена')
    photo = models.ImageField(upload_to='images/mother/', verbose_name='Изображение материнской платы')

class Order(models.Model):
    price = models.IntegerField(verbose_name='Цена')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    id_client = models.IntegerField(verbose_name='Идентификатор клиента')
    id_proc = models.IntegerField(blank=True, verbose_name='Идентификатор процессора')
    id_video = models.IntegerField(blank=True, verbose_name='Идентификатор видеокарты')
    id_mother = models.IntegerField(blank=True, verbose_name='Идентификатор материнской платы')
