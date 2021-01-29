from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ChoiceList, CreateVote, PollViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    # path('polls/', PollList.as_view(), name='polls_list'),
    # path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',
        CreateVote.as_view(), name='create_vore'),
]

urlpatterns += router.urls
