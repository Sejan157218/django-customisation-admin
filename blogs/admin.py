from django.contrib import admin
from .models import Post,Category
import django.apps 



models=django.apps.apps.get_models()



class BlogAdminArea(admin.AdminSite):
    site_header="Blog Site Header"
blog_site=BlogAdminArea(name="BlogAdminArea")

for model in models:
    try:
        blog_site.register(model)
    except blog_site.AlreadyRegistered:
        pass


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields=['title']
# blog_site.register(Post,PostAdmin)


# admin site
admin.site.register(Post)
