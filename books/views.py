from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView

# Create your views here.
def books_main(request):
    books = Articles.objects.all()
    return render(request, 'books/books.html', {'books_key': books})

class BooksDetail(DetailView):
    model = Articles
    template_name = 'books/books_view.html'
    context_object_name = 'article'

class BooksUpdate(UpdateView):
    model = Articles
    template_name = 'books/create.html'
    
    # form_class = ArticlesForm
    fields = ['title', 'author', 'text', 'date']

def create(request):
    err = ''
    if request.method == 'POST':
        #получение данных из формы по POST
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            err = 'Invald data'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': err
    }

    return render(request, 'books/create.html', data)