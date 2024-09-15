from rest_framework import serializers
from .models import Estudante

class EstudanteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)
    cpf = serializers.CharField(max_length=11)
    data_nascimento = serializers.DateField()
    celular = serializers.CharField(max_length=14)
    
    def create(self, validated_data):
        return Estudante.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
        instance.celular = validated_data.get('celular', instance.celular)
        instance.save()
        return instance