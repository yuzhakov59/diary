from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

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