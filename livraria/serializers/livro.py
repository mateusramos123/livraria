from rest_framework.serializers import ModelSerializer
from livraria.models import Livro
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .autor import AutorSerializer

class LivroSerializer(ModelSerializer):        
    class Meta:
        model = Livro
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1         

class LivroListSerializer(ModelSerializer):
    class Meta: 
        model = Livro
        fields = ["id", "titulo", "preco"]          
