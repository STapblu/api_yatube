from django.urls import path, include  # type:ignore
from rest_framework.authtoken.views import obtain_auth_token  # type:ignore
from rest_framework.routers import DefaultRouter  # type:ignore
from .views import PostViewSet, GroupViewSet, CommentViewSet  # type:ignore


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),

    path(
        'posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post-comments'
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='post-comment-detail'
    ),
]
