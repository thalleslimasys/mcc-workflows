from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^workflows/records$", views.Workflow.as_view(), name="workflows"),
]
