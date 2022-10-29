import imp
from django.contrib import admin
from django.urls import path
from blogs.admin import blog_site
from bookstore.admin import bookStore_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
    path('bookstoreadmin/',bookStore_site.urls)

]


# admin.site.index_title="The Book Store"
# admin.site.site_header="Book Store Admin"
# admin.site.site_title="site title admin "
