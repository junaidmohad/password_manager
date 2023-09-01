from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}                    #this means that password only allowed to be written and not read when called upon this class
        }

    def create(self, validated_data):                   #this function sits between the view and the model creation whenever we want to create a new user
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)            #https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters#:~:text=The%20double%20%2A%2A%20means%20there%20can%20be%20any,can%20be%20invoked%20like%20bar%20%281%2C%20a%3D2%2C%20b%3D3%29.
        if password is not None:
            instance.set_password(password)                 #this line shows that django provides in-built hasing of the password, usefull to display in the database and the maybe the frontend
        instance.save()
        return instance