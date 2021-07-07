from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Processor)
admin.site.register(Videocard)
admin.site.register(Motherboard)
admin.site.register(Order)