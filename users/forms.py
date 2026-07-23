from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'phone', 'country','avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите логин для сайта'  # Текст подсказки внутри поля
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите адрес почты'  # Текст подсказки внутри поля
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите пароль'  # Текст подсказки внутри поля
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Подтвердите пароль'  # Текст подсказки внутри поля
        })

        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите номер телефона'  # Текст подсказки внутри поля
        })

        self.fields['country'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите страну'  # Текст подсказки внутри поля
        })

        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Загрузите аватар'  # Текст подсказки внутри поля
        })