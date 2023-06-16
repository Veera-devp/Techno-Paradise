from django.urls import path
from .views import home, upload_image
from .views import about
from .views import contact
urlpatterns = [
    path(' ',home,name='home'),
    path('upload_img', upload_image, name='upload_image'),
     path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
