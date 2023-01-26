from django.urls import include, path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import MyTokenObtainPairView, UsersAPIView

urlpatterns = [
    path('', UsersAPIView.as_view()),
    path('login/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
