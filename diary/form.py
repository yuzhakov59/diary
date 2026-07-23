from django import forms
from django.core.exceptions import ValidationError


from .models import DiaryPost


class DiaryPostForm(forms.ModelForm):
    class Meta:
        model = DiaryPost
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(DiaryPostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите название заголовока'  # Текст подсказки внутри поля
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Содержимое'  # Текст подсказки внутри поля
        })


class DiaryPostModeratorForm(forms.ModelForm):
    class Meta:
        model = DiaryPost
        fields = ['title', 'content']



    def clean_name(self):
        name = self.cleaned_data.get('title')
        banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        name_lower = name.lower()

        for word in banned_words:
            if word in name_lower:
                raise ValidationError('Наименование не должно содержать запрещенных слов')
        return name
