from django.db import models
from django.db.models.deletion import PROTECT, SET_NULL

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
    def __str__(self):
        return '{0}. {1} {2}'.format(self.id, self.name, self.surname)

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
    def __str__(self):
        return '{0}. {1} {2}'.format(self.id, self.manufacturer, self.model)

class Videocard(models.Model):
    manufacturer = models.CharField(max_length=15, verbose_name='Производитель')
    model = models.CharField(max_length=25, verbose_name='Модель')
    memory_type = models.CharField(max_length=6, verbose_name='Тип памяти')
    memory_size = models.IntegerField(verbose_name='Количество памяти')
    quantity = models.IntegerField(verbose_name='Количество на складе')
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='images/video/', verbose_name='Изображение видеокарты')
    def __str__(self):
        return '{0}. {1} {2}'.format(self.id, self.manufacturer, self.model)

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
    def __str__(self):
        return '{0}. {1} {2}'.format(self.id, self.manufacturer, self.model)

class Order(models.Model):
    price = models.IntegerField(verbose_name='Цена')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    id_client = models.ForeignKey(Client, on_delete=PROTECT, verbose_name='Клиент', null=True)
    id_proc = models.ForeignKey(Processor, on_delete=SET_NULL, verbose_name='Процессор', null=True, blank=True)
    id_video = models.ForeignKey(Videocard, on_delete=SET_NULL, verbose_name='Видеокарта', null=True, blank=True)
    id_mother = models.ForeignKey(Motherboard, on_delete=SET_NULL, verbose_name='Материнская плата', null=True, blank=True)

