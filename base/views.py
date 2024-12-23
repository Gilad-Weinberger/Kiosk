from django.shortcuts import render
from .models import Order, RabbiOrderBurgers, RabbiOrderHotdogs
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def add_done_materials(add1: str, list1: list):
    if not add1 in list1:
        list1.append(add1)
    return list1

@csrf_exempt
def create(request):
    materials_done = []
    context = {}

    active_rabbi_order_burgers = RabbiOrderBurgers.objects.filter(is_done=False).first()
    active_rabbi_order_hotdogs = RabbiOrderHotdogs.objects.filter(is_done=False).first()

    if not active_rabbi_order_burgers:
        add_done_materials("המבורגרים", materials_done)
    if not active_rabbi_order_hotdogs:
        add_done_materials("נקנקיות", materials_done)

    if request.method == 'POST':
        name = request.POST.get('name')
        food = request.POST.get('food')
        pay = request.POST.get('pay')

        if not name:
            context["error"] = "שם הוא שדה חובה"
            return render(request, 'create.html', context)

        if pay == 'NOTE':
            if food == 'BURGER':
                if not active_rabbi_order_burgers:
                    if materials_done:
                        materials_done_str = " ו".join(materials_done)
                        context["error"] = f"אין יותר הזמנות של {materials_done_str} עם שוברים"
                    context["fail"] = "אין שוברים להמבורגרים!"
                    return render(request, 'create.html', context)
                active_rabbi_order_burgers.left -= 1
                if active_rabbi_order_burgers.left == 0:
                    active_rabbi_order_burgers.is_done = True
                    add_done_materials("המבורגרים", materials_done)
                active_rabbi_order_burgers.save()
            elif food == 'HOTDOG':
                if not active_rabbi_order_burgers:
                    if materials_done:
                        materials_done_str = " ו".join(materials_done)
                        context["error"] = f"אין יותר הזמנות של {materials_done_str} עם שוברים"
                    context["fail"] = "אין שוברים לנקנקיות!"
                    return render(request, 'create.html', context)
                active_rabbi_order_hotdogs.left -= 1
                if active_rabbi_order_hotdogs.left == 0:
                    active_rabbi_order_hotdogs.is_done = True
                    add_done_materials("נקנקיות", materials_done)
                active_rabbi_order_hotdogs.save()

        new_order = Order.objects.create(name=name, food=food, pay=pay)
        if new_order:
            if new_order.food == 'BURGER':
                new_food = "המבורגר"
            elif new_order.food == 'HOTDOG':
                new_food = "נקנקיה"
            else:
                new_food = "סודוך"
            context["success"] = f"הזמנת {new_food} של {new_order.name} נוצרה בהצלחה"

    if materials_done:
        materials_done_str = " ו".join(materials_done)
        context["error"] = f"אין יותר הזמנות של {materials_done_str} עם שוברים"
        
    return render(request, 'create.html', context)
