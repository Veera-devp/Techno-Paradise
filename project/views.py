from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image_url = settings.MEDIA_URL + str(image.image.url)
            return render(request, 'project/upload_success.html', {'image_url': image_url})
    else:
        form = ImageUploadForm()
    return render(request, 'project/upload_image.html', {'form': form})

def about(request):
    return render(request, 'project/about.html')

def contact(request):
    return render(request, 'project/contact.html')

def home(request):
    return render(request,'project/base.html')