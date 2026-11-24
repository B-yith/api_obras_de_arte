from django.db import models


class ObraArte(models.Model):

    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=150)

    artista = models.CharField(max_length=150)

    ano_criacao = models.IntegerField(
        null=True,
        blank=True
    )

    movimento_artistico = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    tecnica = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    museu = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    pais_origem = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    descricao = models.TextField(
        null=True,
        blank=True
    )

    valor_estimado = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'obras_arte'
        managed = False

    def __str__(self):
        return self.nome