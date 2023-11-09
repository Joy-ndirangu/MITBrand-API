from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from rest_framework import routers

from API.views import Products

router = routers.DefaultRouter()


router.register("products",Products)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)