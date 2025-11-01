from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from.views import JournalDetailAPIView
from.views import JournalUpdateAPIView 
from .views import JournalCreateAPIView
from .views import JournalDestroyAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('journals/<int:pk>/', JournalDetailAPIView.as_view(), name='journal-detail-api'),
    path('journals/<int:pk>/', JournalUpdateAPIView.as_view(), name='journal-update-api'),
    path('journals/<int:pk>/', JournalCreateAPIView.as_view(), name='journal-update-api'),
    path('journals/<int:pk>/', JournalDestroyAPIView.as_view(), name='journal-destroy-api')
]

