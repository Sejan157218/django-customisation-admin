from django.contrib import admin
from .models import *



class BlogAdminArea(admin.AdminSite):
    site_header="Blog Site Header"
blog_site=BlogAdminArea(name="BlogAdminArea")

blog_site.register(Post)


# admin site
admin.site.register(Post)
