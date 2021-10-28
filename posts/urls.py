from django.conf.urls import url
from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^$',views.posts_list,name="list"),
    url(r'^create/$',views.post_create,name="create"),
    url(r'^saved/$',views.saved_post,name="savedpost"),
    url(r'^userpost/$',views.user_post,name="userpost"),
    url(r'^(?P<name>[\w+\s*]+)/$',views.Post_detail,name="detail"),
    url(r'^saved/(?P<name>[\w+\s*]+)/$',views.saved_detail,name="saved"),
    url(r'^userpost/(?P<name>[\w+\s*]+)/edit/$',views.user_post_edit,name="user_post_edit"),
    url(r'^userpost/(?P<name>[\w+\s*]+)/$',views.user_post_detail,name="user_post_detail"),
    #url parameters are captured by p<>
]