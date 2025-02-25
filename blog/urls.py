from django.urls import path
from .views import index, blog, detail


urlpatterns = [
    path("", index),
    path('blog/', blog),
    path('blog/detail/<int:pk>/', detail)
]
