from django.urls import path

from PBI.views import backlog_view, add_view, edit_view, delete_view, create_sprint, add_PBI_to_current_sprint, movePBIdown, movePBIup

urlpatterns = [
    path('', backlog_view, name='backlog'),
    path('add/',add_view, name='add'),
    path('edit/<int:id>',edit_view, name='edit'),
    path('delete/<int:id>',delete_view, name='delete'),
    path('createSprint/', create_sprint, name='create_sprint'),
    path('addPBIToCurrentSprint/<int:id>', add_PBI_to_current_sprint, name="add_PBI_to_current_sprint"),
    path('movePBIup/<int:id>', movePBIup, name='movePBIup'),
    path('movePBIdown/<int:id>', movePBIdown, name='movePBIdown'),
]
