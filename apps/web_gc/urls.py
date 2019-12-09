from django.urls import path

from . import views


urlpatterns = [
    path('patrimonio/gc/', views.view_menu_principal, name='gc_menu_principal'),
    path('patrimonio/gc/menu-cadastros/', views.view_menu_cadastros, name='gc_menu_cadastros'),
    path('patrimonio/gc/menu-cadastros/cadastro-talao/', views.view_cadastrar_talao, name='gc_cadastro_talao'),
    path(
        'patrimonio/gc/menu-cadastros/cadastro-combustivel/',
        views.view_cadastrar_combustivel,
        name='gc_cadastro_combustivel'
    ),
    path('patrimonio/gc/menu-cadastros/cadastro-posto/', views.view_cadastrar_posto, name='gc_cadastro_posto'),
    path('patrimonio/gc/menu-consultas/', views.view_menu_consultas, name='gc_menu_consultas'),
    path('patrimonio/gc/menu-consultas/consulta-taloes/', views.view_taloes, name='gc_consulta_taloes'),
    path(
        'patrimonio/gc/menu-consultas/consulta-taloes/talao=<int:talao_id>/',
        views.view_talao,
        name='gc_consulta_talao'
    ),
    path('patrimonio/gc/menu-consultas/consulta-vales/', views.view_vales, name='gc_consulta_vales'),
    path('patrimonio/gc/menu-consultas/consulta-meus-vales/', views.view_meus_vales, name='gc_consulta_meus_vales'),
    path('patrimonio/gc/menu-relatorios/', views.view_menu_relatorios, name='gc_menu_relatorios'),
    path('patrimonio/gc/menu-relatorios/mensal', views.view_relatorio_mensal, name='gc_relatorio_mensal'),
    path('patrimonio/gc/menu-taloes/', views.view_menu_taloes, name='gc_menu_taloes'),
    path('patrimonio/gc/menu-taloes/entrega-talao/', views.view_entrega_talao, name='gc_entrega_talao'),
    path('patrimonio/gc/menu-vales/', views.view_menu_vales, name='gc_menu_vales'),
    path('patrimonio/gc/menu-vales/entrega-vale-1/', views.view_entrega_vale_1, name='gc_entrega_vale_1'),
    path('patrimonio/gc/menu-vales/entrega-vale-2/', views.view_entrega_vale_2, name='gc_entrega_vale_2'),
]
