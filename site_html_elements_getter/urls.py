from django.urls import path

from site_html_elements_getter.views import TagsView

urlpatterns = [
    path('tags/', TagsView.as_view()),
    path('tags/<task_id>', TagsView.as_view()),
]
