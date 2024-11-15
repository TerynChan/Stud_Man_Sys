from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_user, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('register/', views.register_user, name= 'register'),
    path('add_student/', views.add_student, name= 'add_student'),
    path('student/<int:id>', views.student_card, name= 'view_student'),
    path('search_student/', views.search_student, name= 'search_student'),
    path('edit_student/<int:id>', views.edit_student, name= 'edit_student'),
    path('delete_student/<int:id>', views.delete_student, name= 'delete_student'),
    
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)