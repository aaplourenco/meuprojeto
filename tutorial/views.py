from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tutorial_termux_setup(request):
    return render(request, 'tutorial_termux_setup.html')

def tutorial_vscode_setup(request):
    return render(request, 'tutorial_vscode_setup.html')

def tutorial_html_css_js_basics(request):
    return render(request, 'tutorial_html_css_js_basics.html')

def tutorial_git_github_intro(request):
    return render(request, 'tutorial_git_github_intro.html')

def tutorial_python_fundamentals(request):
    return render(request, 'tutorial_python_fundamentals.html')

def tutorial_sqlite_sqlalchemy(request):
    return render(request, 'tutorial_sqlite_sqlalchemy.html')