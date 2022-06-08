import string
import random


class EmailValidator:
    ALLOWED_SYMBOLS = string.ascii_letters + string.digits + '_.@'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        """
        - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точка и собачка @ (одна);
        - длина email до символа @ не должна превышать 100 (сто включительно);
        - длина email после символа @ не должна быть больше 50 (включительно);
        - после символа @ обязательно должна идти одна точка;
        - не должно быть двух точек подряд.
        """
        cls.__is_email_str(email)
        if [ch in cls.ALLOWED_SYMBOLS for ch in email] and \
            len(email.split('@')[0]) <= 100 and len(email.split('@')[1]) and \
            '.' in email.split('@')[1] and \
            not '..' in email:
            return True
        else:
            return False

    @classmethod
    def get_random_email(cls):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 100))) + '@.gmail.com'
    
    def __is_email_str(email):
        return isinstance(str, type(email))


#print(EmailValidator.check_email('test@test..ru'))
#print(EmailValidator.get_random_email())
