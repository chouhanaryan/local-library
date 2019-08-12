from django.shortcuts import render
<<<<<<< HEAD
from catalog.models import Book, Author, BookInstance, Genre, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
=======
from catalog.models import Book, Author, BookInstance, Genre
>>>>>>> 966a25c7653f18d6992532af252992869a4dcce5

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()
    
<<<<<<< HEAD
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

=======
>>>>>>> 966a25c7653f18d6992532af252992869a4dcce5
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
<<<<<<< HEAD
        'num_visits': num_visits,
=======
>>>>>>> 966a25c7653f18d6992532af252992869a4dcce5
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

<<<<<<< HEAD
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).order_by('status')

class BookListView(generic.ListView):
    '''default context is sent to book_list.html as book_list'''
    model = Book
    paginate_by = 5
    # queryset = Book.objects.filter(language='English')

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    '''default context is sent to author_list.html as author_list'''
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

def genre_list_view(request):
    genre_list = Genre.objects.all()

    context = {'genre_list': genre_list}

    return render(request, 'genre_list.html', context)

class GenreDetailView(generic.DetailView):
    model = Genre

class LanguageListView(generic.ListView):
    model = Language

class LanguageDetailView(generic.DetailView):
    model = Language
=======
def books(request):
	book_list = []
	for x in list(Book.objects.all()):
		book_list.append(x.title)

	context = {
		'book_list': book_list
	}
	return render(request, 'books.html', context=context)
>>>>>>> 966a25c7653f18d6992532af252992869a4dcce5
