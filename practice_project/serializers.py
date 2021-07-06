from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from firstapp.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'price', 'date', 'id_client_id', 'id_proc_id', 'id_video_id', 'id_mother_id']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'surname', 'patronymic', 'phone_number', 'city', 'street', 'house', 'flat', 'email', 'password']

class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = ['id', 'manufacturer', 'model', 'frequency', 'socket', 'cores', 'threads', 'quantity', 'price']

class VideocardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videocard
        fields = ['id', 'manufacturer', 'model', 'memory_type', 'memory_size', 'quantity', 'price']

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = ['id', 'manufacturer', 'model', 'socket', 'chipset', 'memory_slots', 'max_memory_frequency', 'quantity', 'price']