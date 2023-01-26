from django.urls import include, path
from .views import UsersAPIView

urlpatterns = [
    path('', UsersAPIView.as_view()),
]
