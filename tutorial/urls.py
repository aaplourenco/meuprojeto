from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tutorial_termux_setup/', views.tutorial_termux_setup, name='tutorial_termux_setup'),
    path('tutorial_vscode_setup/', views.tutorial_vscode_setup, name='tutorial_vscode_setup'),
    path('tutorial_html_css_js_basics/', views.tutorial_html_css_js_basics, name='tutorial_html_css_js_basics'),
    path('tutorial_git_github_intro/', views.tutorial_git_github_intro, name='tutorial_git_github_intro'),
    path('tutorial_python_fundamentals/', views.tutorial_python_fundamentals, name='tutorial_python_fundamentals'),
    path('tutorial_sqlite_sqlalchemy/', views.tutorial_sqlite_sqlalchemy, name='tutorial_sqlite_sqlalchemy')
]
