from celery import shared_task
from sms import send_sms


@shared_task()
def send_confirmation_code_task(phone_number, code):
    """Отправляет СМС с кодом подтверждения."""
    send_sms(f'Ваш код: {code}', recipients=[phone_number])
