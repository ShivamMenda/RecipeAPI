from django.urls import path,include # noqa
from rest_framework.routers import DefaultRouter # noqa
from recipe import views # noqa

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('recipes',views.RecipeViewSet)
router.register('tags',views.TagViewSet)
router.register('ingredients',views.IngredientViewSet)

urlpatterns = [
    path('',include(router.urls))
]
