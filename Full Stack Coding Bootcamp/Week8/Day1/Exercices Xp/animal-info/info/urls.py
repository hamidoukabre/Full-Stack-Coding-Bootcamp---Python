from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('family/<int:x>', views.family, name="family" ),
    path('animal/<int:y>', views.animals, name="animal")
]










