from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from brokerApp.form import *
from brokerApp.models import *


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'brokerApp/home.html'
    login_url = 'brokerApp:login'


class ClienteListView(ListView):
    model = Cliente
    template_name = 'brokerApp/listar_clientes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['list_url'] = reverse_lazy('brokerApp:cliente_listar')
        context['entity'] = 'Clientes'
        context['form'] = ClienteForm()
        return context

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('brokerApp:cliente_listar')

class PolizaListView(ListView):
    model = Poliza
    template_name = 'brokerApp/listar_polizas.html'

class PolizaCreateView(CreateView):
    model = Poliza
    form_class = PolizaForm
    success_url = reverse_lazy('brokerApp:poliza_listar')