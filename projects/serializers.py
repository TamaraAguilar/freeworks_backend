from rest_framework import serializers
from .models import Project, Deliverable, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class DeliverableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverable
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    progress = serializers.ReadOnlyField(source='calculate_progress')
    deliverables = DeliverableSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'client', 'status', 'priority', 'created_at', 'progress', 'deliverables', 'comments']