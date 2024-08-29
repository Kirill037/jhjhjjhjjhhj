from django.urls import path, re_path
from . import views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('delete_favorite/<int:favorite_id>/', views.delete_favorite, name='delete_favorite'),
    # Add this line to serve favicon.ico
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/ico/favicon.ico', permanent=True)),
]


# Add this line to serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
