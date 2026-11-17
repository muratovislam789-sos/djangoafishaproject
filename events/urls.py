from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/add/', EventCreateView.as_view(), name='event_create'),
]
