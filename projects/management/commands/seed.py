from django.core.management.base import BaseCommand
from projects.models import Project, Deliverable

class Command(BaseCommand):
    help = 'Puebla la base de datos con datos de prueba para el MVP'

    def handle(self, *args, **kwargs):
        self.stdout.write("Limpiando registros anteriores...")
        Project.objects.all().delete()

        self.stdout.write("Generando proyectos...")
        p1 = Project.objects.create(name='Infraestructura Cloud', client='TechCorp', status='Progreso', priority='Alta')
        p2 = Project.objects.create(name='Motor de Base de Datos', client='Finanzas SA', status='Atrasado', priority='Media')
        p3 = Project.objects.create(name='Portal de Usuarios', client='Retail SPA', status='Finalizado', priority='Baja')

        self.stdout.write("Generando entregables...")
        Deliverable.objects.create(project=p1, title='Topología de Red', description='Diseño de VPC', due_date='2026-09-10', status='Entregado')
        Deliverable.objects.create(project=p1, title='Contenedores Docker', description='Imágenes base', due_date='2026-09-15', status='Pendiente')
        Deliverable.objects.create(project=p2, title='Migración PL/SQL', description='Scripts de datos', due_date='2026-09-01', status='Atrasado')
        Deliverable.objects.create(project=p3, title='Componentes Angular', description='Vistas UI', due_date='2026-08-20', status='Entregado')

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada exitosamente!'))