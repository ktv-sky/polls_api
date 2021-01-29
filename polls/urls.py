from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from .views import ChoiceList, CreateVote, LoginView, PollViewSet, UserCreate


API_TITLE = 'Polls API'
API_DESCRIPTION = 'A Web API for creating and editing polls.'

swagger_view = get_swagger_view(title=API_TITLE)

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',
        CreateVote.as_view(), name='create_vore'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),

]

urlpatterns += router.urls

urlpatterns += [
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    path('swagger-docs/', swagger_view),
]
