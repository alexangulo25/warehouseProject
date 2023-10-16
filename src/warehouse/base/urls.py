from django.urls import path
from .views import WarehouseView, itemDetail, createRecord, editRecord, deleteRecord, Login, RegisterPage, subir_archivo
from django.contrib.auth.views import LogoutView


urlpatterns = [path('', WarehouseView.as_view(), name='warehouse_main'),
               path('login/', Login.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('register/', RegisterPage.as_view(), name='register'),
               path('item/<int:pk>', itemDetail.as_view(), name='itemID'),
               path('create-record/', createRecord.as_view(), name='create-record'),
               path('edit/<int:pk>', editRecord.as_view(), name='edit'),
               path('delete/<int:pk>', deleteRecord.as_view(), name='delete'),
               path('subir_archivo/', subir_archivo, name='subir_archivo'),]