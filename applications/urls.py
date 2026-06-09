from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:internship_id>/', views.apply_internship, name='apply'),

    path('my/', views.my_applications, name='my_applications'),

    path('company/', views.company_applications, name='company_applications'),

    path('<int:app_id>/<str:status>/', views.update_application, name='update_application'),

    path('notifications/read/', views.mark_notifications_read, name='mark_notifications_read'),
]