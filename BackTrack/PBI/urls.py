from django.urls import path

from PBI.views import backlog_view, add_view, detail_view, delete_view

urlpatterns = [
    path('', backlog_view, name='backlog'),
    path('add/',add_view, name='add'),
    path('detail/<int:id>',detail_view, name='detail'),
    path('delete/<int:id>',delete_view, name='delete'),
]
