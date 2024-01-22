from django.contrib import admin
from .models import Progress,WorkMan,Completed,Pre_completed
# Register your models here.
admin.site.register(Progress)
admin.site.register(WorkMan)
admin.site.register(Completed)
admin.site.register(Pre_completed)
