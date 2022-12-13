from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("school/", include("school.urls")),
    path("mongo_school/", include("school.mongo_urls")),
]
