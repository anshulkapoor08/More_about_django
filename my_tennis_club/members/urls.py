from django.urls import path # type: ignore
from . import views # type: ignore

urlpatterns = [
    
    path('testing/',views.testing, name='testing'), # type: ignore
    path('',views.main, name='main'), # type: ignore
    path('members/',views.members, name='members'), # type: ignore
    path('members/details/<int:id>',views.details, name = 'details')
]    
