from django.contrib import admin

from .models import txt_file

# Register your models here.

@admin.register(txt_file)
class txt_file_admin(admin.ModelAdmin):
   list_display=['id','txtfile']
