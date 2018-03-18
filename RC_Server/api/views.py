from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
import json
from rest_framework.views import APIView
from rest_framework import parsers, renderers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response


# Create your views here.

@csrf_exempt
def signup(request):
    try:
        with transaction.atomic():
            user = User()
            user.username = request.POST.get('username')
            user.password = make_password(request.POST.get('password'), salt=None, hasher='default')
            user.email = request.POST.get('email')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()

        return HttpResponse(
            json.dumps(
                {
                    'token': Token.objects.get(user=user).key
                }
            )
        )
    except Exception as e:
        return HttpResponse(
            json.dumps(
                {
                    'error': str(e)
                }
            )
        )


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user)
        user_name = str(User.objects.get(username=user).first_name) + ' ' + str(
            User.objects.get(username=user).last_name)
        print(user_name)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'username': user_name
            }
        )


obtain_auth_token = ObtainAuthToken.as_view()
