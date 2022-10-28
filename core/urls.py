from django.contrib import admin
from django.urls import path
from blogs.admin import blog_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/',  ),

]


# admin.site.index_title="The Book Store"
# admin.site.site_header="Book Store Admin"
# admin.site.site_title="site title admin "
