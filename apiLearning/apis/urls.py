from .views import *
from django.urls import path,include
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r"companies",viewset=comapanyViewSet)
router.register(r"employee",employeeViewSet)
urlpatterns=[
    path("",include(router.urls))
]   

