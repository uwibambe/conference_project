from django.urls import path
from speaker import views

urlpatterns = [
    path('speakers/', views.speaker_view),
    path('speakers/create', views.create_speaker_view),
    path('speakers/<id>' , views.speaker_id ),
    path('speakers/<speaker_id>/update', views.speaker_update),
    path('speakers/<speaker_id>/delete', views.speaker_delete),

]