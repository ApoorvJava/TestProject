from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'fruits', views.FruitsViewSet)
router.register(r'vegetables', views.VegetablesViewSet)
router.register(r'beautyproducts', views.BeautyProductsViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))

]
