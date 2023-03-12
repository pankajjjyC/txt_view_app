from django.shortcuts import render
from my_view.models import txt_file
from django.conf import settings
import os

# Create your views here.

def index(r):     
    return render(r,'index.html',{})

def read_file(r):
    if r.method == 'POST':# csv file saving code
        file = r.FILES['myfile']        
        id = r.POST['id']
        obj = txt_file(txtfile=file,id=id)
        obj.save()

        txt_file_obj=txt_file.objects.first()
        file_selected=txt_file_obj.txtfile

        with open(os.path.join(settings.MEDIA_ROOT,
                                   f"{obj.txtfile}"), 'r') as f:
                content = f.read()

        return render(r, "index.html", {
                
                "content": content
            })
