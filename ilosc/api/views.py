from rest_framework import generics
from ..models import Stat
from .serializers import StatSerializer
from django.db.models import Count
from ..models import Word_freq
from .serializers import Word_freqSerializer
from .serializers import User1Serializer
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
from .serializers import User2Serializer
from .serializers import User3Serializer
from .serializers import User4Serializer
from .serializers import User5Serializer
from .serializers import User6Serializer
from .serializers import User7Serializer
from .serializers import User8Serializer
from .serializers import User9Serializer
from .serializers import User10Serializer

class StatListView(generics.ListAPIView):
    queryset = Stat.objects.raw("SELECT * FROM Stat")
    serializer_class = StatSerializer


class Word_freqListView(generics.ListAPIView):
    queryset = Word_freq.objects.raw("SELECT * FROM Word_freq")
    serializer_class = Word_freqSerializer

class User1ListView(generics.ListAPIView):
    queryset = User1.objects.raw("SELECT * FROM User1")
    serializer_class = User1Serializer

class User2ListView(generics.ListAPIView):
    queryset = User2.objects.raw("SELECT * FROM User2")
    serializer_class = User2Serializer

class User3ListView(generics.ListAPIView):
    queryset = User3.objects.raw("SELECT * FROM User3")
    serializer_class = User3Serializer

class User4ListView(generics.ListAPIView):
    queryset = User4.objects.raw("SELECT * FROM User4")
    serializer_class = User4Serializer

class User5ListView(generics.ListAPIView):
    queryset = User5.objects.raw("SELECT * FROM User5")
    serializer_class = User5Serializer

class User6ListView(generics.ListAPIView):
    queryset = User6.objects.raw("SELECT * FROM User6")
    serializer_class = User6Serializer

class User7ListView(generics.ListAPIView):
    queryset = User7.objects.raw("SELECT * FROM User7")
    serializer_class = User7Serializer

class User8ListView(generics.ListAPIView):
    queryset = User8.objects.raw("SELECT * FROM User8")
    serializer_class = User8Serializer

class User9ListView(generics.ListAPIView):
    queryset = User9.objects.raw("SELECT * FROM User9")
    serializer_class = User9Serializer

class User10ListView(generics.ListAPIView):
    queryset = User10.objects.raw("SELECT * FROM User10")
    serializer_class = User10Serializer