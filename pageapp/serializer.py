from rest_framework import serializers
from .models import postclass,User


class postclassserializer(serializers.ModelSerializer):
    class Meta:
        model = postclass
        fields=['id','name','course','date','sign','fileup']
#-------------------------------------------------------------------------------------------------------------------        
# usersignserializer----------------------------------------------        
class signinserializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},max_length=200)
    class Meta:
        model = User
        fields=['name','email','password','password2']
        extra_kwargs={'password':{'write_only':True}}
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
    def validate(self, data):
        password=data.get('password')
        password2=data.get('password2')
        if password != password2:
            raise serializers.ValidationError("password doenot match")
        return data    
#userloginserializer------------------------------------------------

class loginserializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = User
        fields=['email','password']        
        
#usergetserializer------------------------------------------------ 
class usergetserializer(serializers.ModelSerializer):
    class Meta:
        model = postclass
        fields= ['name','course','date','sign','fileup']    
        
        