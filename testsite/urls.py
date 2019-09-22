from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from shiptrader.urls import router

urlpatterns = [url(r'^admin/', admin.site.urls), url(r'^api/v1/', include(router.urls))]

# docs views https://github.com/axnsan12/drf-yasg#id7
schema_view = get_schema_view(
    openapi.Info(
        title='Snippets API',
        default_version='v1',
        description='Starship Marketplace API',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@snippets.local'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
