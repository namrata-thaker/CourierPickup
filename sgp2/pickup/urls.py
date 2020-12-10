from django.urls import include,path
from . import views

app_name = 'pickup'

urlpatterns = [
    path('form/',views.form),
    path('form/shipment/',views.shipment),
    path('form/shipment/success/',views.success, name='success'),
    path('order/',views.order),
    path('header/',views.header),

]

