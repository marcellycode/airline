# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Página inicial
def index(request):
    if not request.user.is_authenticated:  # Verificando se o usuário está autenticado
        return redirect("login")  # Redireciona para a página de login
    return render(request, "users/user.html")  # Renderiza a página inicial

# Página de login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Autentica o usuário
            return redirect("index")  # Redireciona para a página inicial
        else:
            return render(request, "users/login.html", {"error": "Usuário ou senha inválidos."})
    return render(request, "users/login.html")  # Exibe o formulário de login

# Página de logout
def logout_view(request):
    logout(request)  # Desloga o usuário
    return render(request, "users/login.html",{
        "message": "Logged out"
    })
# Redireciona para a página de login
    
