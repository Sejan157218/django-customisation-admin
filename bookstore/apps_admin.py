from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig



class BookStoreAdminConfig(AdminConfig):
    default_site="bookstore.admin.bookStore_site"

    
class BookstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookstore'
