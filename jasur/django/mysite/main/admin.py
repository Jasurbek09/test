from django.contrib import admin
from main.models import Author, Book, Country, Chelsea


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


class ChelseaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chelsea, ChelseaAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
