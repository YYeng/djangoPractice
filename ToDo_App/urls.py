from django.urls import path

from . import views

urlpatterns = [
    path('', views.item_list, name='home-page'),
    path('add_item/', views.add_form, name='add_form'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),

]
