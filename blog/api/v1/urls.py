from . import views
from django.urls import path,include

app_name = "api-v1"
urlpatterns = [

    path('post/',views.PostList,name="post-list"),
    path('post/<int:id>/',views.PostDetail,name="post-detail")

    ]