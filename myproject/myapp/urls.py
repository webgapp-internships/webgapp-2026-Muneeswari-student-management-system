from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',views.index, name='index'),
    path('about/',views.about,name='about/'),
    path('contact/',views.contact,name='contact/'),
    path('table/',views.table,name='table'),
     path('testing/',views.testing,name='testing'),
      path('main/',views.main,name='main'),
       path('sample/',views.sample,name='sample'),
     
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
