
# Lab1_Mazur - Google QUEST Q&A Labeling

Цей проєкт є реалізацією моделі машинного навчання для участі в змаганні [Google QUEST Q&A Labeling](https://www.kaggle.com/competitions/google-quest-challenge). Метою є покращення автоматизованого розуміння складного контенту запитання-відповідь за допомогою сучасних NLP-підходів.

## 📁 Структура ноутбуку

1. **Install and Import Library**  
   Встановлення та імпорт необхідних бібліотек (`transformers`, `datasets`, `sklearn`, `torch` тощо).

2. **Import Data**  
   Завантаження навчального, тестового та прикладеного файлів через `pandas`.

3. **Tokenizer & DataLoader**  
   Токенізація тексту за допомогою Hugging Face токенізатора (`AutoTokenizer`) та побудова `DataLoader` об'єктів.

4. **Model**  
   Імплементація кастомної регресійної моделі на базі `BertModel`, яка передбачає одночасно кілька вихідних тегів.

5. **Optimizer & Scheduler**  
   Налаштування оптимізатора (`AdamW`) та планувальника навчальної ставки (`get_linear_schedule_with_warmup`).

6. **Training**  
   Процедура навчання з виведенням функції втрат та метрик для валідації.

7. **Submission**  
   Побудова фінального сабмішну в `.csv` форматі для завантаження на Kaggle.

## 🧪 Використані технології

- Python 3.x
- PyTorch
- Hugging Face Transformers
- Scikit-learn
- Pandas / NumPy
- Kaggle API

## 🏁 Результати

- ✅ **Публічний скор (Public Score):** `0.31051`
- 🔒 **Приватний скор (Private Score):** `0.27740`
- 🕒 Сабміт здійснено після дедлайну (late submission)

[screenshot](/NLP/Lab1/Pasted image.png)

---

_Лабораторна робота виконана у межах курсу з обробки природної мови._
