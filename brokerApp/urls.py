from django.urls import path
from django.contrib.auth import views as auth_views

from brokerApp.views import Home, ClienteListView, ClienteCreateView, PolizaListView, PolizaCreateView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='brokerApp/login.html'), name='login'),
    path('login/', auth_views.LogoutView.as_view(template_name='brokerApp/login.html'), name='logout'),
    path('clientes/listar/', ClienteListView.as_view(), name='cliente_listar'),
    path('clientes/crear/', ClienteCreateView.as_view(), name='cliente_crear'),
    path('polizas/listar/', PolizaListView.as_view(), name='poliza_listar'),
    path('polizas/crear/', PolizaCreateView.as_view(), name='poliza_crear'),
]