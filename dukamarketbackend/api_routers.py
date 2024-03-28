from rest_framework.routers import DefaultRouter
from product import urls as product_urls


app_name = "api_routers"

routers = DefaultRouter()

routers.registry.extend(product_urls.router.registry)

routers.urls.extend(product_urls.router.urls)

urlpatterns = routers.urls
