from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.TextField(max_length=500, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.role_name}"

    class Meta:
        unique_together = ('role_name', 'description')

class Speciality(models.Model):
    speciality_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.TextField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.speciality_name}"

    class Meta:
        verbose_name_plural = _("Specialities")
        unique_together = ('speciality_name', 'description')

class Lane(models.Model):
    lane_name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.TextField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.lane_name}"

    class Meta:
        unique_together = ('lane_name', 'description')

class Hero(models.Model):
    hero_id = models.IntegerField(unique=True)
    hero_name = models.CharField(max_length=50)
    hero_alias = models.CharField(max_length=50)
    hero_slug = models.SlugField(unique=True, db_index=True)
    primary_role: Role = models.ForeignKey("hero.Role", on_delete=models.CASCADE, related_name='primary_role')
    secondary_role: Role = models.ForeignKey("hero.Role", on_delete=models.CASCADE, null=True, blank=True, related_name='secondary_role')
    primary_speciality: Speciality = models.ForeignKey("hero.Speciality", on_delete=models.CASCADE, related_name='primary_speciality')
    secondary_speciality: Speciality = models.ForeignKey("hero.Speciality", on_delete=models.CASCADE, null=True, blank=True, related_name='secondary_speciality')
    primary_lane: Lane = models.ForeignKey("hero.Lane", on_delete=models.CASCADE, related_name='primary_lane')
    secondary_lane: Lane = models.ForeignKey("hero.Lane", on_delete=models.CASCADE, null=True, blank=True, related_name='secondary_lane')

    @property
    def roles(self):
        if self.secondary_role != None:
            return f"{self.primary_role} / {self.secondary_role}"
        else:
            return f"{self.primary_role}"

    @property
    def specialities(self):
        if self.secondary_speciality != None:
            return f"{self.primary_speciality} / {self.secondary_speciality}"
        else:
            return f"{self.primary_speciality}"
        
    @property
    def lanes(self):
        if self.secondary_lane != None:
            return f"{self.primary_lane} / {self.secondary_lane}"
        else:
            return f"{self.primary_lane}"

    def clean(self):
        if self.primary_role == self.secondary_role:
            raise ValidationError("Primary role and secondary role cannot be the same.")
        if self.primary_speciality == self.secondary_speciality:
            raise ValidationError("Primary speciality and secondary speciality cannot be the same.")
        if self.primary_lane == self.secondary_lane:
            raise ValidationError("Primary lane and secondary lane cannot be the same.")
        super().clean()

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        if self.hero_slug == None:
            name_alias = self.hero_name + ' the ' + self.hero_alias
            self.hero_slug = slugify(name_alias)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.hero_name}, the {self.hero_alias}"

    class Meta:
        verbose_name_plural = _("Heroes")
        unique_together = ('hero_name', 'hero_alias', 'hero_slug')

class HeroRatings(models.Model):
    hero: Hero = models.OneToOneField("hero.Hero", related_name='hero_ratings', on_delete=models.CASCADE)
    durability = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    offense = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    control_effects = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    difficulty = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self) -> str:
        return f"{self.hero.hero_name}"

    class Meta:
        verbose_name_plural = _("Heroes Ratings")

# class HeroStats(models.Model):
#     health = models.IntegerField()
#     mana = models.IntegerField()
#     health_regen = models.FloatField()
#     mana_regen = models.FloatField()