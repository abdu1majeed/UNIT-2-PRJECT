# SaudiaArabia/context_processors.py
def theme_context(request):
    theme = request.COOKIES.get("theme", "light")
    if theme not in ("light", "dark"):
        theme = "light"
    return {"theme": theme}