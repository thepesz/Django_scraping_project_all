from rest_framework import serializers
from ..models import Stat
from ..models import Word_freq
from ..models import User1
from ..models import User2
from ..models import User3
from ..models import User4
from ..models import User5
from ..models import User6
from ..models import User7
from ..models import User8
from ..models import User9
from ..models import User10

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ('word', 'author')

class Word_freqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word_freq
        fields = ('word', 'quantity')


class User1Serializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = ('word', 'quantity')

class User2Serializer(serializers.ModelSerializer):
    class Meta:
        model = User2
        fields = ('word', 'quantity')

class User3Serializer(serializers.ModelSerializer):
    class Meta:
        model = User3
        fields = ('word', 'quantity')

class User4Serializer(serializers.ModelSerializer):
    class Meta:
        model = User4
        fields = ('word', 'quantity')

class User5Serializer(serializers.ModelSerializer):
    class Meta:
        model = User5
        fields = ('word', 'quantity')

class User6Serializer(serializers.ModelSerializer):
    class Meta:
        model = User6
        fields = ('word', 'quantity')

class User7Serializer(serializers.ModelSerializer):
    class Meta:
        model = User7
        fields = ('word', 'quantity')

class User8Serializer(serializers.ModelSerializer):
    class Meta:
        model = User8
        fields = ('word', 'quantity')

class User9Serializer(serializers.ModelSerializer):
    class Meta:
        model = User9
        fields = ('word', 'quantity')

class User10Serializer(serializers.ModelSerializer):
    class Meta:
        model = User10
        fields = ('word', 'quantity')