from django.urls import path
from . import views

urlpatterns = [
    path('', views.internship_list, name='internship_list'),
    path('<int:internship_id>/', views.internship_detail, name='internship_detail'),
    path('create/', views.create_internship, name='create_internship'),
    path('<int:internship_id>/edit/', views.edit_internship, name='edit_internship'),
    path('<int:internship_id>/delete/', views.delete_internship, name='delete_internship'),
    path('<int:internship_id>/toggle/', views.toggle_status, name='toggle_status'),
]