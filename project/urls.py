from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("admin/",admin.site.urls),
    path("", include("app.urls"))
    # path("", LPU, name="render")
    # path("about", aboutLPU, name="about"),
    # path("aboutme", aboutme, name="me")
]
