from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Sender)
admin.site.register(Category)
admin.site.register(Receiver)
admin.site.register(ReceiverCategory)
admin.site.register(Template)
admin.site.register(History)
