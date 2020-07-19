from django.urls import path
from . import views

app_name = 'names'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.name_add, name='add'),


    path('<int:pk>/update', views.NameUpdate.as_view(), name='update'),
    #path('<int:pk>/edit', views.EditView.as_view(), name='edit'),

]