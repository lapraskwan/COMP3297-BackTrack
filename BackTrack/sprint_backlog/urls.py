from django.urls import path

from sprint_backlog.views import backlog_view,add_view,delete_view,edit_view,pushPBIBack_view

urlpatterns = [
    path('', backlog_view, name='backlog'),
    path('add/<int:id>', add_view, name='add'),
    path('delete/<int:id>', delete_view, name='delete'),
    path('update/<int:id>', edit_view, name='edit'),
    path('pushPBIBack/<int:id>', pushPBIBack_view, name='pushPBIBack'),
]
