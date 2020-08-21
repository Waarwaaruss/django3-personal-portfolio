from django.shortcuts import render, get_object_or_404
from .models import Gallery

def gallery(request): 
    galleries = Gallery.objects.all()
    return render(request, 'gallery/gallery.html', {'galleries': galleries})

def details(request, gallery_id):
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    return render(request, 'gallery/details.html',{'gallery':gallery})