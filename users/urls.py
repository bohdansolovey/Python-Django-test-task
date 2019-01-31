from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import refresh_jwt_token

from users import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/posts', views.PostByAuthor.as_view(),name='user-post-list'),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('refresh-token/', refresh_jwt_token),
]
urlpatterns = format_suffix_patterns(urlpatterns)