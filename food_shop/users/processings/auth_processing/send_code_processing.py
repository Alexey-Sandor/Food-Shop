from users.tasks import send_confirmation_code_task
from users.utils import generate_confirmation_code


def send_code_at_form_valid(request, form):
    """Отправляет код подтверждения после валидации формы.

    Генерирует код, сохраняет номер и код в сессию.
    Вызывает таск на отправку кода на номер телефона юзера.
    """
    phone_number = form.cleaned_data['phone_number']
    code = generate_confirmation_code()
    request.session['code'] = code
    request.session['phone_number'] = phone_number
    send_confirmation_code_task.delay(phone_number, code)
