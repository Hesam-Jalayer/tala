from django.urls import path
from .views import (
    MilliGoldList,
    TlynList,
    TalaseList
)


urlpatterns = [
    path('mili-gold', MilliGoldList.as_view()),
    path('tlyn', TlynList.as_view()),
    path('talase', TalaseList.as_view())
]
