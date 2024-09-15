from rest_framework import serializers
from .models import Estudante, Curso, Matricula
    
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'celular']

    
    
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'descricao', 'nivel']
    
    def validate_nivel(self, value):
        """Valida e converte 'Básico', 'Intermediário', 'Avançado' para 'B', 'I', 'A'."""
        nivel_map = dict(Curso.NIVEL_CHOICES)
        reverse_nivel_map = {v: k for k, v in nivel_map.items()}
        
        if value not in reverse_nivel_map:
            raise serializers.ValidationError(
                'Nível inválido, escolha entre: {}'.format(', '.join(reverse_nivel_map.keys()))
            )
        
        return reverse_nivel_map[value]
    
    def to_representation(self, instance):
        """Converte 'B', 'I', 'A' para 'Básico', 'Intermediário', 'Avançado'."""
        representation = super().to_representation(instance)
        nivel_map = dict(Curso.NIVEL_CHOICES)
        
        representation['nivel'] = nivel_map.get(instance.nivel, instance.nivel)
        
        return representation
    
    
    
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['id', 'estudante', 'curso', 'periodo']
    
    
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()
    
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']