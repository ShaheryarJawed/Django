from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stock_app.views import UserViewSet, StockViewSet, TransactionViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Create a router for the API endpoints
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'stocks', StockViewSet, basename='stock')
router.register(r'transactions', TransactionViewSet, basename='transaction')

# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="Stock Transactions API",
        default_version='v1',
        description="API documentation for managing users, stocks, and transactions",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site path
    path('api/', include(router.urls)),  # API endpoints path
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI path
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Optionally, Redoc UI path
]
