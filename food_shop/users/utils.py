from random import choices


def generate_confirmation_code():
    """Генерирует код подтверждения из 6 цифр"""
    return ''.join(choices('0123456789', k=6))
