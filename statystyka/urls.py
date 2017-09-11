from django.conf.urls import url
from ilosc import views
from django.conf.urls import include



urlpatterns = [
    url(r'^test/', views.scrap),
    url(r'^api/', include('ilosc.api.urls', namespace='api')),
]
