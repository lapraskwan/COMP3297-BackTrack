from django.urls import path

from PBI.views import backlog_view, add_view, edit_view, delete_view

urlpatterns = [
    path('', backlog_view, name='backlog'),
    path('add/',add_view, name='add'),
    path('edit/<int:id>',edit_view, name='edit'),
    path('delete/<int:id>',delete_view, name='delete'),
]
