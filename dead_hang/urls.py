from django.urls import path
from . import views

from django.views.generic import TemplateView

app_name = 'dead_hang'

urlpatterns = [
    path('', views.index, name='index'),
    path('stats/', views.stats, name='stats'),
    path('api/save/', views.save_result, name='save_result'),
    path('api/clear/', views.clear_data, name='clear_data'),
    path('service-worker.js', TemplateView.as_view(template_name="dead_hang/service-worker.js", content_type='application/javascript'), name='service_worker'),
    path('manifest.json', TemplateView.as_view(template_name="dead_hang/manifest.json", content_type='application/json'), name='manifest'),
]
