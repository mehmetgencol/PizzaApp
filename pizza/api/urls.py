from django.conf.urls import url, include
from . import views

app_name = 'api'

urlpatterns = [
	url(r'^get_pizza/', views.get_pizza, name='get_pizza'),
    url(r'^add_pizza/', views.add_pizza, name='add_pizza'),
    url(r'^delete_pizza/', views.delete_pizza, name='delete_pizza'),
    url(r'^update_pizza/', views.update_pizza, name='update_pizza'),
]
