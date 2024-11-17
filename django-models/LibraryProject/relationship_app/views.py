from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# Create your views here.
Book.objects.all()
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('home')  # Redirect to home or another view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})        

from django.contrib.auth.decorators import user_passes_test

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})
def is_admin(user):
    if not user.is_authenticated:
        return False
    try:
        return user.profile.role == 'Admin'
    except AttributeError:
        return False
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})    