from django.db import models

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=250)
    activo=models.BooleanField(default=True)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo=models.CharField(max_length=250)
    nombre=models.CharField(max_length=250)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    marca=models.CharField(max_length=250)
    descripcion=models.TextField(blank=True, null=True)
    precio=models.FloatField()
    categorias=models.ForeignKey(CategoriaProd,on_delete=models.CASCADE)
    destacado=models.BooleanField(default=True)
    descuento=models.BooleanField(default=True)
    activo=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre