from django.urls import path

from .views import CurrentDateView, RandView, Hello, IndexView

urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('random/', RandView.as_view()),
   path('hello/', Hello.as_view()),
   path('indexview/', IndexView.as_view())
]
