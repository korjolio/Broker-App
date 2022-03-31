from pyexpat import model
from django.forms import  *

from brokerApp.models import *


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('tipo_pers', 'nombre', 'rut', 'direccion', 'ciudad', 'comuna', 'region', 'email', 'telefono', 'celular')
        template_name = 'brokerApp/cliente_form.html'
        widgets = {
            'tipo_pers': RadioSelect(
            ),
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'rut': TextInput(
                attrs={
                    'class': 'form-control',
                    'oninput': "checkRut(this)"
                },
            ),
            'direccion': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'region': Select(
                attrs={
                    'class': 'form-control select2',
                }
            ),
            'ciudad': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comuna': Select(
                attrs={
                    'class': 'form-control select2',
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'celular': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

class PolizaForm(ModelForm):
    class Meta:
        model = Poliza
        fields = ('moneda', 'cliente', 'nro_poliza', 'ini_vig', 'fin_vig', 'producto', 'pri_afe', 'pri_exe', 'pri_net', 'pri_iva', 'pri_bru', 'vigente')
        template_name = 'brokerApp/poliza_form.html'
        widgets = {
            'moneda': RadioSelect(
            ),
            'cliente': Select(
                attrs={
                    'class': 'form-control select2',
                }
            ),
            'nro_poliza': TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
           
            'producto': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        
        }


