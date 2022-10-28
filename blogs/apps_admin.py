from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class BlogAdminConfig(AdminConfig):
    default_site= 'blogs.admin.BlogAdminArea'



class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'
