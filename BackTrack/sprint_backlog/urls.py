from django.urls import path

from . import views

urlpatterns = [
    path('', views.showAll, name='showAll'),
    path('add/<int:id>', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('pushPBIBack/<int:id>', views.pushPBIBack, name='pushPBIBack'),
]
