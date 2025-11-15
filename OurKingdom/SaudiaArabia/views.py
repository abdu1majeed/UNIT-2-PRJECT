from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def home_page(request:HttpRequest):
    return render(request, "SaudiaArabia/home.html")

def history_page(request:HttpRequest):
    return render(request, "SaudiaArabia/history.html")

def tourism_page(request:HttpRequest):
    return render(request, "SaudiaArabia/tourism.html")

def culture_page(request:HttpRequest):
    return render(request, "SaudiaArabia/culture.html")

def manufacturing_page(request:HttpRequest):
    return render(request, "SaudiaArabia/manufacturing.html")

def vision_page(request:HttpRequest):
    return render(request, "SaudiaArabia/vision.html")

def education_page(request:HttpRequest):
    return render(request, "SaudiaArabia/education.html")


from django.http import HttpResponseRedirect
from django.urls import reverse

THEME_COOKIE_NAME = "theme"
THEME_MAX_AGE = 60 * 60 * 24 * 365  # سنة

def _redirect_back(request, default_name="SaudiaArabia:home_page"):
    next_url = request.GET.get("next") or request.META.get("HTTP_REFERER")
    if not next_url:
        next_url = reverse(default_name)
    return HttpResponseRedirect(next_url)

def toggle_theme(request):
    current = request.COOKIES.get(THEME_COOKIE_NAME, "light")
    new_theme = "dark" if current != "dark" else "light"
    resp = _redirect_back(request)
    resp.set_cookie(THEME_COOKIE_NAME, new_theme, max_age=THEME_MAX_AGE, samesite="Lax")
    return resp

def set_theme(request, mode):
    mode = (mode or "").lower()
    if mode not in ("light", "dark"):
        mode = "light"
    resp = _redirect_back(request)
    resp.set_cookie(THEME_COOKIE_NAME, mode, max_age=THEME_MAX_AGE, samesite="Lax")
    return resp