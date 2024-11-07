from django.db import models

class Review(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=20)  # Поле для хранения тональности ("положительный" или "отрицательный")

    def __str__(self):
        return self.text[:50]  # Для отображения первых 50 символов отзыва
