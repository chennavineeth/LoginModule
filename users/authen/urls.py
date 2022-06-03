from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView ,TokenRefreshView)



urlpatterns=[ 
    path('register/',views.RegisterApiView.as_view(),name='register'),
    path('token/',TokenObtainPairView.as_view(),name='token'),
    path('token/refresh/',TokenRefreshView.as_view(),name='tokenrefersh'),
    path('verified',views.DetailsAPIView.as_view(),name='verified'),
    path('login/',views.DetailsAPIView.as_view(),name="login"),
    path('sign/',views.LoginAPIView.as_view(),name='sign'),
]