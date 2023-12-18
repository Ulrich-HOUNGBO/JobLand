from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="JobLand API",
        #  version of the swagger doc
        default_version='v0',
        # first line that appears on the top of the doc
        description="Api for JobLand",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('JobList.urls'), name='job'),
    path('', include('jobApplication.urls'), name='jobApplication'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)