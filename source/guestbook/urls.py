from django.urls import path
from guestbook.views import index_view

urlpatterns = [
    path('', index_view, name='list'),
    path('entries/', index_view, name='list'),
    path('entries/add', index_view, name='add'),
    ]