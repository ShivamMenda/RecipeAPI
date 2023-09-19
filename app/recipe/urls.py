from django.urls import path,include # noqa
from rest_framework.routers import DefaultRouter # noqa
from recipe import views # noqa

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('',views.RecipeViewSet)


urlpatterns = [
    path('recipes/',include(router.urls))
]
