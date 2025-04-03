from django.urls import path
from blog.views import indexs, about, add_post

app_name = "blog"
urlpatterns = [
    path("about/", about, name="about"),
    path("post/", add_post, name="add_post"),
    path("", index, name="index")
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
if settings.DEBUG:
    urlpatterns += ststic(settigs.MEDIA_URL, document_root = settings.MEDIA_ROOT)