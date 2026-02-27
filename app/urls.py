from django.urls import path
from .views import LPU, aboutView, saveDataView, delete, updateViewpage, updateDataView


urlpatterns = [
    path("", LPU, name="index"),
    path("about", aboutView, name="aboutLPU"),
    path("save_data",saveDataView, name="save_data"),
    # path("delete", delete, name="delete"),
    path("delete/<int:id>", delete, name="delete"),
    path("update-note/<int:id>", updateViewpage, name="updateViewpage"),
    path("update-data/<int:id>", updateDataView, name="updateDataView"),
]