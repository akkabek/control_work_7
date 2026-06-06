from django.urls import path
from guestbook.views import index_view, entry_edit_view, entry_create_view, entry_delete_view

urlpatterns = [
    path('', index_view, name='list'),
    path('entries/', index_view, name='list'),
    path('entries/add', entry_create_view, name='add'),
    path('entries/edit/<int:pk>', entry_edit_view, name='edit'),
    path('entries/delete/<int:pk>', entry_delete_view, name='delete'),
    ]