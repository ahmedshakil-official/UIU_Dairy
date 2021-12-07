from django.urls import path
from . import views

app_name = 'f'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('detail/<pk>/', views.Details.as_view(), name='detail'),
    path('add', views.Add.as_view(), name='add'),
    path('update/<pk>', views.Update.as_view(), name='update'),
    path('delete/<pk>', views.Delete.as_view(), name='delete'),
]