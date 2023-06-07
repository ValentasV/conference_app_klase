from django.urls import path
from Renginys.views import RenginysDetailView, RegisterVisitorView, UserEventList

urlpatterns = [
    path("<int:pk>/", RenginysDetailView.as_view(), name = 'event-detail'),
    path("register/<int:renginio_id>/", RegisterVisitorView.as_view(), name = 'register-visitor'),
    path("my-events/", UserEventList.as_view(), name = "user-events"),
]