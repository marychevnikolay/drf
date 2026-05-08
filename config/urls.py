
from django.contrib import admin
from django.urls import include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include, re_path
from api_project.views import  *
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)
# router = routers.SimpleRouter()
# router.register(r'cooking', CookingViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
    
   path('api/v1/cooking/',  CookingAPIList.as_view()),
   path('api/v1/cooking/<int:pk>/',  CookingAPIUpdate.as_view()),
   path('api/v1/cooking/<int:pk>/',  CookingAPIDestroy.as_view()),

   path('api/v1/auth/', include('djoser.urls')),
   re_path(r'^auth/', include('djoser.urls.authtoken')),

   path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/v1/token/verify', TokenVerifyView.as_view(), name='token_verify'),
        
        
]
