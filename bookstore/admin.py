from django.contrib import admin

class BookStoreAdminArea(admin.AdminSite):
    site_header="Book Site Header"

bookStore_site=BookStoreAdminArea(name="bookstorearea")


