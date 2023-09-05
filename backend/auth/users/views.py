# from django.shortcuts import render

from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework import viewsets

# Create your views here.
class RegisterView(viewsets.ViewSet):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(viewsets.ViewSet):
    def post(self, request):
        email =  request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()     #line to find the user with respect the email of the user   

        if user is None:
            raise AuthenticationFailed('No user found')
        
        if not user.check_password(password):                   #since the password is hashed
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {                     #in jwt there is something important called as payload required for the jwt token generation
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),       #this line sets the expiration time for the token
            'iat': datetime.datetime.utcnow()               #this sets the tiem when the jwt token is generated
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')        #should'nt we add .decode() after this but it shows error

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)          #set_cookie() is a method of Response() and setting the httponly to true means that the frontend cant access the token
 
        response.data = {
            "jwt": token
        }

        return response

class UserView(viewsets.ViewSet):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:                   #if we dont find any token
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms = ['HS256'])           #note it should be algorithms and not algorithm because we need to pass a list of algorithms for decoding
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)



        return Response(serializer.data)

class LogoutView(viewsets.ViewSet):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "success"
        }

        return response