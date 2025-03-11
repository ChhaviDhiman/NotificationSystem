from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def home(request):
    return HttpResponse("<h1>Welcome to the Notification System API</h1>")

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('api/', include('notifications.urls')),  # Make sure 'notifications.urls' is included here
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
