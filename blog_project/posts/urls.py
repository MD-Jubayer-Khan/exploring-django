from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_post, name='add-post'),
    path('edit_post/<int:id>', views.edit_post, name='edit-post'),
    path('delete_post/<int:id>', views.delete_post, name='delete-post')
]