from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [('Progreso', 'En progreso'), ('Finalizado', 'Finalizado'), ('Atrasado', 'Atrasado')]
    PRIORITY_CHOICES = [('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')]
    
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Progreso')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Media')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def calculate_progress(self):
        total = self.deliverables.count()
        if total == 0:
            return 0
        delivered = self.deliverables.filter(status='Entregado').count()
        return round((delivered / total) * 100, 2)

class Deliverable(models.Model):
    STATUS_CHOICES = [('Pendiente', 'Pendiente'), ('Entregado', 'Entregado'), ('Atrasado', 'Atrasado')]
    
    project = models.ForeignKey(Project, related_name='deliverables', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendiente')
    simulated_file = models.URLField(blank=True, null=True)

class Comment(models.Model):
    project = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)