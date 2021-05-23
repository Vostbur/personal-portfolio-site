from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work/', views.work, name='work'),
    path('work/<int:id>/', views.work_detail, name='work_detail'),
    path('about/', views.about, name='about'),
]
