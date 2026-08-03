from django.urls import path

from .views import OperationView


urlpatterns = [

    path(
        "operations/",
        OperationView.as_view(),
        name="operations",
    ),

]