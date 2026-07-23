import json
import random

from django.http import HttpResponse
from django.utils import timezone

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from diary.form import DiaryPostForm
from diary.models import DiaryPost


class DiaryPostListView(ListView):
    model = DiaryPost

    def get_context_data(self, **kwargs):
        """
        Добавляет мотивирующую фразу в контекст для шаблона.
        """
        context = super().get_context_data(**kwargs)

        motivating_phrase = ""
        try:
            phrases_file_path = './static/motivating_phrases.json'

            with open(phrases_file_path, 'r', encoding='utf-8') as f:
                phrases_list = json.load(f)
                if phrases_list:
                    motivating_phrase = random.choice(phrases_list)

        except FileNotFoundError:
            motivating_phrase = "Файл с мотивирующими фразами не найден."
        except json.JSONDecodeError:
            motivating_phrase = "Ошибка при чтении мотивирующих фраз (некорректный JSON)."
        except Exception as e:
            motivating_phrase = f"Произошла ошибка: {e}"

        context['motivating_phrase'] = motivating_phrase

        current_date = timezone.now().strftime('%d %B %Y')
        context['current_date'] = current_date
        return context


class DiaryPostDetailView(DetailView):
    model = DiaryPost


class DiaryPostCreateView(LoginRequiredMixin, CreateView):
    model = DiaryPost
    form_class = DiaryPostForm
    success_url = reverse_lazy('diary:diary_list' )

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)


class DiaryPostUpdateView(LoginRequiredMixin, UpdateView):
    model = DiaryPost
    form_class = DiaryPostForm
    success_url = reverse_lazy('diary:diary_list' )


class DiaryPostDeleteView(DeleteView):
    model = DiaryPost
    success_url = reverse_lazy('diary:diary_list' )


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse("Данные отправлены!")
    return render(request,'diary/contacts.html' )
