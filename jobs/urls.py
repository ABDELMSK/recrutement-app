# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('job/list', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/create/', views.job_create, name='job_create'),
    path('job/<int:pk>/update/', views.job_update, name='job_update'),
    path('job/<int:pk>/delete/', views.job_delete, name='job_delete'),
    path('<int:job_id>/apply/', views.apply_to_job, name='apply_to_job'),

]

