from django.utils import translation
from django.http import HttpResponseRedirect
from django.conf import settings


class LanguageRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path_parts = request.path.split('/')
        if path_parts[1] not in [lang[0] for lang in settings.LANGUAGES]:
            user_language = request.META.get("HTTP_ACCEPT_LANGUAGE", "")
            user_language = user_language.split(",")[0][:5].lower()

            if user_language not in [lang[0] for lang in settings.LANGUAGES]:
                user_language = settings.LANGUAGE_CODE

            translation.activate(user_language)
            request.LANGUAGE_CODE = user_language

            return HttpResponseRedirect(f'/{user_language}{request.path}')
            
        response = self.get_response(request)   
        return response