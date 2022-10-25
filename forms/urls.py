from django.urls import path
from . import views
from .views import HomePageView,RegisterView,EditDataView


urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='home'),
    path('add_data/',RegisterView.as_view(), name='add-vehicle'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:pk>', EditDataView.as_view(), name='update'),


]