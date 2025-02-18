from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection
from .models import NoticiaImportada  # Importando o modelo da notícia

@receiver(post_save, sender=NoticiaImportada)
def processar_noticia_nova(sender, instance, created, **kwargs):
    """
    Executa a Stored Procedure VincularNoticiasAClientes sempre que uma nova notícia for cadastrada.
    """
    if created:  # Somente quando a notícia for criada (não para edições)
        with connection.cursor() as cursor:
            cursor.execute("EXEC VincularNoticiasAClientes;")  # Chama a SP
