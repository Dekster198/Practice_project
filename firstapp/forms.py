from django import forms
from django.forms import fields
from .models import *

class AddProc(forms.ModelForm):
    class Meta:
        model = Processor
        fields = ['manufacturer', 'model', 'frequency', 'socket', 'cores', 'threads', 'quantity', 'price', 'photo']

class AddVideo(forms.ModelForm):
    class Meta:
        model = Videocard
        fields = ['manufacturer', 'model', 'memory_type', 'memory_size', 'quantity', 'price', 'photo']

class AddMother(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = ['manufacturer', 'model', 'socket', 'chipset', 'memory_slots', 'max_memory_frequency', 'quantity', 'price', 'photo']

class AddClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'patronymic', 'phone_number', 'city', 'street', 'house', 'flat', 'email', 'password']

class AddOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['price', 'id_client', 'id_proc', 'id_video', 'id_mother']


class DelProc(forms.Form):
    id = forms.IntegerField()

class DelVideo(forms.Form):
    id = forms.IntegerField()

class DelMother(forms.Form):
    id = forms.IntegerField()

class DelClient(forms.Form):
    id = forms.IntegerField()

class DelOrder(forms.Form):
    id = forms.IntegerField()
    