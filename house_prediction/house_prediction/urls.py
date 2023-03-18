from django.urls import include, path

urlpatterns = [
    path('', include('house.urls')),
]
