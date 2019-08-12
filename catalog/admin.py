from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language

<<<<<<< HEAD

# Register using decorator (before the class as a wrapper) - @admin.register(class)
# Register traditionally (after the class) - admin.site.register(model class, related admin class) 


=======
>>>>>>> 966a25c7653f18d6992532af252992869a4dcce5
class BooksInstanceInline(admin.TabularInline):
    '''to display book instance information with book information during book creation'''
    model = BookInstance

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('title', 'author', 'language', 'display_genre')
=======
    list_display = ('title', 'author', 'display_genre', 'language')
>>>>>>> 966a25c7653f18d6992532af252992869a4dcce5
    list_filter = ('genre', 'language')
    inlines = [BooksInstanceInline] # refer above class


class AuthorInstanceInline(admin.TabularInline):
    '''to display book information with author information during author creation'''
    model = Book

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), 'date_of_birth', 'date_of_death']
    # exclude = ['date_of_death']
    inlines = [AuthorInstanceInline] # refer above class
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('book', 'id', 'borrower', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
          (None, {'fields': ('book', 'id')}),
            ('Availability', {'fields': ('status', 'due_back', 'borrower',)})
        )
    # if (BookInstance.LOAN_STATUS == 'o'):
    #     fieldsets = (
    #     	(None, {'fields': ('book', 'imprint', 'id')}),
    #         ('Availability', {'fields': ('status', 'due_back',)})
    #     )
    # else:
    #     fieldsets = (
    #         (None, {'fields': ('book', 'imprint', 'id')}),
    #         ('Availability', {'fields': ('status',)})
    #     )
=======
    list_display = ('book', 'id', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
    	(None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')})
    )
>>>>>>> 966a25c7653f18d6992532af252992869a4dcce5

admin.site.register(Language)