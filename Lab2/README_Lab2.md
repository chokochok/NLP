
# Lab2 – Fine-Tuning BERT and LLaMA Classifiers

Цей проєкт є частиною лабораторної роботи з обробки природної мови, в якій реалізовано fine-tuning моделей BERT та LLaMA для задачі класифікації на основі тексту. Референтною точкою для оцінювання виступає STEAM baseline модель.

## 📁 Структура ноутбуків

### 🔷 `Lab2_bert.ipynb`
1. **Imports** – імпорт бібліотек (Hugging Face, PyTorch, sklearn).
2. **Load Model** – завантаження BERT-моделі для класифікації.
3. **Zero eval** – базова оцінка до навчання.
4. **Fine tune model** – навчання моделі з логуванням до `wandb`.
5. **Final eval** – підсумкова оцінка на валідаційному наборі.
![screenshot](/Lab2/wand_bert/Pastedimage.png)
![screenshot](/Lab2/wand_bert/Pastedimage(2).png)

### 🔷 `Lab2_llama.ipynb`
1. **Setup and Installation** – середовище, бібліотеки (`transformers`, `trl`, `peft`).
2. **Load the Language Model** – завантаження LLaMA-моделі (через `AutoModelForCausalLM`).
3. **Apply PEFT** – застосування методів параметрично-ефективного навчання (LoRA).
4. **Prepare the Dataset** – обробка та токенізація даних.
5. **Inference with Streaming (pre-training)** – оцінка до навчання.
6. **Configure the DPO Trainer** – налаштування Direct Preference Optimization.
7. **Start Training** – запуск fine-tuning із логуванням на wandb.
8. **Save the Model Locally** – збереження моделі.
9. **Load Saved Model** – перевірка збереженої моделі.
10. **Inference with Streaming (post-training)** – фінальна оцінка.
![screenshot](/Lab2/wand_llama/Pastedimage.png)
![screenshot](/Lab2/wand_llama/Pastedimage(2).png)
![screenshot](/Lab2/wand_llama/Pastedimage(3).png)

### 🔷 `Lab2_steam.ipynb`
- Містить референсну модель STEAM, яка використовується для порівняння точності з fine-tuned версіями BERT та LLaMA.

## 🧪 Технології

- Transformers (Hugging Face)
- PEFT + LoRA
- TRL (Transformer Reinforcement Learning)
- PyTorch
- Weights & Biases (wandb)
- Datasets
- CUDA (при доступності)

## 📊 Логування результатів

- Проміжні метрики логуються у **Weights & Biases**.
- Додано скріншоти з `wandb` у репозиторій (`training_curve.png`, `eval_metrics.png`, тощо).

## 📈 Порівняння моделей

| Модель      | До навчання (zero-shot) | Після fine-tuning | Коментар                        |
|-------------|-------------------------|--------------------|--------------------------------|
| STREAM      | 0.84                    | -                  | Базова модель                  |
| BERT        | 0.36                    | 0.56               | Класичний fine-tune            |
| LLaMA 3.2-1B| 0.42                    | 0.68               | DPO + LoRA, краща генералізація|

---

_Лабораторна робота виконана у межах курсу з обробки природної мови._
