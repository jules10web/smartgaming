from django.shortcuts import render
from django.shortcuts import render
from qrcode.apps import QrcodeConfig
from .models import Room
from base.models import Screen
from qrcode.models import Qrcode
import qrcode
from io import BytesIO
from django.core.files import File
from PIL  import Image, ImageDraw
from base.models import Room



# Create your views here.
def qrc(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), 
              image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context=context["svg"] = stream.getvalue().decode()

    return render(request,'qrcode/qrc.html',context)
    