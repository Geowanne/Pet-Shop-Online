from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, PrimaryKeyRelatedField
#from termios import CDSUSP
from reserva.models import Reserva, Petshop, Categoria
from base.models import Contato  

# Serializers de dados do Petshop
class PetshopNestedModelSeralizer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'

# Serializers de categoria
class CategoriaNestedModelSeralizer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CategoriaModelSerializer(ModelSerializer):
    resrvas = HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name='api:reserva-detail'
)
    class Meta:
        model = Categoria
        fields = '__all__'

class PetshopModelSerializer(ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reserva-detail'
    )

    class Meta:
        model = Petshop
        fields = '__all__'
    
class PetshopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSeralizer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data
    
class CategoriaRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = CategoriaNestedModelSeralizer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data    
    
# Agendamentos
class AgendamentoModelSeralizer(ModelSerializer):
    petshop = PetshopRelatedFieldCustomSerializer(
        queryset = Petshop.objects.all(),
        read_only = False
    )

    categoria = CategoriaRelatedFieldCustomSerializer(
        queryset = Categoria.objects.all(),
        read_only = False
    )

    class Meta:
        model = Reserva
        fields = '__all__'

# Contatos 
class ContatoModelSeralizer(ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'        