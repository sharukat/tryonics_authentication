from django.urls import path
#from authentication.views import  UserLoginAPI
from authentication import views

# ==========================================================================================

urlpatterns = [
    path('helloworld/', views.hello_world, name='helloworld'),
]