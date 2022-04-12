from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.nombre
  
#Crear un nuevo modelo llamado Cliente el cual tendrá como campos: 
# nombres, apellidos, dni, teléfono, dirección, email, fecha de nacimiento y fecha de publicación.   
class Cliente(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.IntegerField(default=0)
    telefono = models.IntegerField(default=0)
    direccion = models.EmailField(max_length=254)
    birth_date = models.DateField('birth date')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return '{} {}'.format( self.nombres,self.apellidos)

 
    