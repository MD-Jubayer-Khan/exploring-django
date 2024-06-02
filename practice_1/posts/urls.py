from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_album, name='add-post'),
    path('edit_album/<int:id>', views.edit_album, name='edit-album'),
    path('delete_album/<int:id>', views.delete_album, name='delete-album')
]