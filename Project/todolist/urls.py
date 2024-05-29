from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add, name='addtask'),
    path('view/', views.view, name='viewtasks'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('base/', views.base, name='base'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
