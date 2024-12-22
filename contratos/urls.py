from django.urls import path
from . import views

urlpatterns = [
    path('contratos/<int:pk>/detail/', views.ErpContratoDetailView.as_view(), name='contrato_detail'),
    path('contratos/<int:cliente_id>/create/', views.ErpContratoCreateView.as_view(), name='contrato_create'),
]