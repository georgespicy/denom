from django.urls import path
from denom.views import home, about, blog, marriage, news, contact, footer, feedback


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("blog/", blog, name="blog"),
    path("marriage/", marriage, name="marriage"),
    path("news/", news, name="news"),
    path("contact/", contact, name="contact"),
    path("footer/", footer, name="footer"),
    path("feedback/", feedback, name="feedback"),
]