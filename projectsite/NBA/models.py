from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator

class BaseModel (models.Model):
    created_at = models.DateTimeField(
    auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True
        
class ProLeague(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
        
class NBAPlayer (BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    college = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class NBATeam(BaseModel):
    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=100, null=True, blank=True)
    years_active = models.CharField(max_length=100, null=True, blank=True)
    league = models.ForeignKey (ProLeague, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} - {self.years_active}"



class Brands (BaseModel):
    brand_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.brand_name} - {self.email}"

    
class Playerscareer (BaseModel):
    Player = models.ForeignKey (NBAPlayer, blank=True, null=True, on_delete=models.CASCADE)
    Team = models.ForeignKey (NBATeam, blank=True, null=True, on_delete=models.CASCADE)
    Seasons = models.IntegerField(blank=True, null=True,validators=[MinValueValidator(0)])
    Brand = models.ForeignKey (Brands, blank=True, null=True, on_delete=models.CASCADE)
    Income = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"{self.Player} - {self.Team} - {self.Seasons} years pro"
