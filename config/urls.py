"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from users.views import UserVerifyView, ProfileView, OrderView, ShopifyView, ShopifyUserProfile, ShopifyUserFiles
from setups.views import ProductTypeView
from content.views import FileModelView, ContentModelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('shopify/', ShopifyView.as_view(), name='shopify_api'),
    path('shopify-profile/<int:pk>/', ShopifyUserProfile.as_view(), name="shopify-profile_api"),
    path('shopify-files/<int:pk>/<str:pk2>/', ShopifyUserFiles.as_view(), name="shopify-file_api"),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

router = DefaultRouter()
router.register('userinfo', UserVerifyView, basename='userinfo_api')
router.register('order', OrderView, basename='order_api')
router.register('profile', ProfileView, basename='profile_api')
router.register('product', ProductTypeView, basename='product_api')
router.register('files', FileModelView, basename='files_api')
router.register('content', ContentModelView, basename='content_api')
urlpatterns += router.urls
