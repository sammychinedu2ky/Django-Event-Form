from django.urls import path

from . import views
app_name='aihacks'
urlpatterns = [
    
    path('',views.IndexView.as_view(),  name='index'),
    path('code',views.code,name='code'),
    
]