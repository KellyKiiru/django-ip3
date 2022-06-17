from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/<user_id>/', views.edit_profile, name='edit_profile'),
    path('project/<post_rated>', views.project, name='project'),
    path('new_post/',views.newpost, name='new_post'),
    path('search/',views.search,name='search'),
    path('api/profile/', views.Profilelist.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)