from django.urls import path # type: ignore
from . import views # type: ignore

urlpatterns = [
    path('members/',views.members, name='members'), # type: ignore
]
