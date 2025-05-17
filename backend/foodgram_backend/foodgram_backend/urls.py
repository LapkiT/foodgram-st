from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from recipes.views import RecipeShortLinkView


urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        's/<str:short_id>/',
        RecipeShortLinkView.as_view(),
        name='short_link_redirect'
    ),

    # Djoser endpoints
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/users/', include('djoser.urls')),
    path('api/', include('api.urls')),
    path('', include('recipes.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
