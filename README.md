###lab4
## Файлы проекта

```
calculator.py          - основной код калькулятора
test_calculator.py     - тесты (5 тестов)
test_plan.md      - план тестирования
```

## Как использовать

### 1. Запуск калькулятора

```python
from calculator import add, subtract, multiply, divide

# Примеры
print(add(5, 3))        # 8
print(subtract(10, 4))  # 6
print(multiply(3, 7))   # 21
print(divide(15, 3))    # 5.0
```

### 2. Запуск тестов

```bash
# Запустить все тесты
python -m unittest test_calculator.py

# Запустить с подробным выводом
python -m unittest test_calculator.py -v

# Запустить один конкретный тест
python -m unittest test_calculator.CalculatorTestCase.test_add
```

## Что тестируется

- ✅ Сложение (add)
- ✅ Вычитание (subtract)
- ✅ Умножение (multiply)
- ✅ Деление (divide)
- ✅ Обработка деления на ноль

## Результаты

**Всего тестов:** 5  
**Пройдено:** 5 ✅  
**Провалено:** 0  

## Документация

- **TEST_PLAN_CALC.md** - подробный план тестирования
---

**Лабораторная работа №4 - Unit тестирование**  
**Автор:** Набиев Денис M3118  
**Дата:** 12.11.2025
