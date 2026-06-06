from django.urls import path
from guestbook.views import index_view, entry_create_view

urlpatterns = [
    path('', index_view, name='list'),
    path('entries/', index_view, name='list'),
    path('entries/add', entry_create_view, name='add'),
    ]