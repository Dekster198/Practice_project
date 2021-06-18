from django.db import models

class Client(models.Model):
    id_client = models.IntegerField()
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=25)
    street = models.CharField(max_length=20)
    house = models.IntegerField()
    flat = models.IntegerField(blank=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Processor(models.Model):
    id_proc = models.IntegerField()
    manufacturer = models.CharField(max_length=15)
    model = models.CharField(max_length=25)
    frequency = models.IntegerField()
    socket = models.CharField(max_length=15)
    cores = models.IntegerField()
    threads = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='images/proc/')

class Videocard(models.Model):
    id_video = models.IntegerField()
    manufacturer = models.CharField(max_length=15)
    model = models.CharField(max_length=25)
    memory_type = models.CharField(max_length=6)
    memory_size = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='images/video/')

class Motherboard(models.Model):
    id_mother = models.IntegerField()
    manufacturer = models.CharField(max_length=15)
    model = models.CharField(max_length=25)
    socket = models.CharField(max_length=15)
    chipset = models.CharField(max_length=15)
    memory_slots = models.IntegerField()
    max_memory_frequency = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='images/mother/')

class Order(models.Model):
    id_order = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    id_client = models.IntegerField()
    id_proc = models.IntegerField(blank=True)
    id_video = models.IntegerField(blank=True)
    id_mother = models.IntegerField(blank=True)

