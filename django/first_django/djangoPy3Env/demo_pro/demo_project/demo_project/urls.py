from django.urls import path, include
# from django.conf.urls import url
# from django.contrib import admin

urlpatterns = [
    path('', include ('first_app.urls')),
    # url(r'^admin/', admin.site.urls),
]