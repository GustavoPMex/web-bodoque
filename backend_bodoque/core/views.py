from django.shortcuts import render
from fotografias.models import Fotografia
# Create your views here.

def index(request):
    foto_obj = Fotografia.objects.all()
    return render(request, 'core/index.html', {'foto_obj':foto_obj})
