from django.shortcuts import render
from .models import Order, RabbiOrder
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def create(request):
    context = {}
    active_rabbi_order = RabbiOrder.objects.filter(is_done=False).first()

    if not active_rabbi_order:
        context["error"] = "אין עוד הזמנות עם שוברים"

    if request.method == 'POST':
        name = request.POST.get('name')
        food = request.POST.get('food')
        pay = request.POST.get('pay')

        if not name:
            context["error"] = "שם הוא שדה חובה"
            return render(request, 'create.html', context)

        if pay == 'NOTE':
            if active_rabbi_order:
                if food == 'BURGER':
                    active_rabbi_order.burgers_left -= 1
                elif food == 'HOTDOG':
                    active_rabbi_order.hotdogs_left -= 1

                active_rabbi_order.save()
            else:
                context["error"] = "!!אין עוד הזמנות עם שוברים"
                return render(request, 'create.html', context)

        new_order = Order.objects.create(name=name, food=food, pay=pay)
        if new_order:
            if new_order.food == 'BURGER':
                new_food = "המבורגר"
            elif new_order.food == 'HOTDOG':
                new_food = "נקנקיה"
            else:
                new_food = "סודוך"
            context["success"] = f"הזמנת {new_food} של {new_order.name} נוצרה בהצלחה"
        
    return render(request, 'create.html', context)
