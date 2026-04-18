from django.db import models

# Create your models here.


class DragCalculation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    air_density = models.FloatField()        # ρ (kg/m³)
    velocity = models.FloatField()           # v (m/s)
    frontal_area = models.FloatField()       # A (m²)
    drag_coefficient = models.FloatField()   # C_w
    drag_force = models.FloatField()         # F_D (N)
    power = models.FloatField()              # P (W)

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M')} - F_D={self.drag_force:.2f} N"

