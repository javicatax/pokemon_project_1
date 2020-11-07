from django.urls import path
from pokemon_api import views
from rest_framework.routers import DefaultRouter
from pokemon_api.views import PokemonesViewSet

# Using router
router = DefaultRouter()
router.register('pokemones', PokemonesViewSet, basename='pokemones', )

# Using Urlpatterns
urlpatterns = [
    path('pokemon_detail/<int:id_pokemon>/', views.PokemonApiView.as_view()),
]

# Add routers to urls form urlpatterns
urlpatterns += router.urls