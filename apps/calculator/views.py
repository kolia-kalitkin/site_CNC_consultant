from django.shortcuts import render


def index(request):
    result = ''
    if request.method == 'POST':
        try:
            num1 = float(request.POST['num1'])
            num2 = float(request.POST['num2'])
            operation = request.POST['operation']

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Ошибка: деление на ноль'
            else:
                result = 'Некорректная операция'
        except ValueError:
            result = 'Ошибка ввода'

    return render(request, 'calculator/index.html', {'result': result})
