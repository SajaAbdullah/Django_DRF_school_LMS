from django.urls import path 

from .views import TeacherView

urlpatterns = [
    path('teacher/', TeacherView.as_view()),
    path('teacher/<uuid:uuid>', TeacherView.as_view()),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]