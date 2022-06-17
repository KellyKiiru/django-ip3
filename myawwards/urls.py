from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    #path('upload/', views.add_post, name='add'),
    path('project/<post_rated>', views.project, name='project'),
    path('new_post/',views.newpost, name='new_post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)