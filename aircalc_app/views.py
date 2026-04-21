from django.shortcuts import render
from .models import DragCalculation


def calculate_drag(request):
    context = {}
    if request.method == "POST":
        rho = float(request.POST.get('air_density'))
        v = float(request.POST.get('velocity'))
        A = float(request.POST.get('frontal_area'))
        Cw = float(request.POST.get('drag_coefficient'))

        # berekening luchtweerstand: F_D = 0.5 * ρ * v² * A * C_w
        drag_force = 0.5 * rho * v ** 2 * A * Cw

        # benodigde vermogen: P = F_D * v
        power = drag_force * v

        # opslaan in database
        DragCalculation.objects.create(
            air_density=rho,
            velocity=v,
            frontal_area=A,
            drag_coefficient=Cw,
            drag_force=round(drag_force, 2),
            power=round(power, 2),
        )

        context['drag_force'] = round(drag_force, 2)
        context['power'] = round(power, 2)
        context['history'] = DragCalculation.objects.all().order_by('-date')[:5]

    return render(request, 'aircalc.html', context)