from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto')

    def __str__(self):
        return self.nome
    
class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Diario(models.Model):
    titulo = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name='diarios')
    pessoas = models.ManyToManyField(Pessoa)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    def get_tags(self):
        return self.tags.all()

    def set_tags(self, list_tags, reset=False):
        if reset:
            self.tags.clear()

        for tag_name in list_tags:
            tag, created = Tag.objects.get_or_create(nome=tag_name)
            self.tags.add(tag)

