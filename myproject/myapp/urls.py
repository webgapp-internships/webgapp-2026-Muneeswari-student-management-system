from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',views.index, name='index'),
    path('about/',views.about,name='about/'),
    path('form/',views.form,name='form'),
    path('form_result/',views.form_result,name='form_result'),
    path('form_edit/<int:id>/', views.form_edit, name='form_edit'),
    path('form_delete/<int:id>/', views.form_delete, name='form_delete'),
    path('contact/',views.contact,name='contact/'),
    path('table/',views.table,name='table'),
    path('service/',views.service,name='service'),
    path('testing/',views.testing,name='testing'),
    path('main/',views.main,name='main'),
    path('sample/',views.sample,name='sample'),
    path('new/',views.new,name='new'),
    path('newabout/',views.newabout,name='newabout'),
    path('newservices/',views.newservices,name='newservices'),
    path('web/',views.web,name='web'),
    path('collections/', views.collections,name='collections'),
    path('gallery/', views.gallery,name='gallery'),
    path('contactin/', views.contactin,name='contactin'),
     
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
