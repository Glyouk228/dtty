import flet as ft
import numpy as np

def calculate_g(d_input, y_input, result_text):
    # Получаем значения d и y из текстовых полей
    d = float(d_input.value)
    y = float(y_input.value)
    
    # Вычисляем R
    R = np.power(np.sin(y), 2) + 0.3 * d / np.exp(y) + np.log10(d)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'R = {R}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №23"
    
    # Создаем текстовые поля для ввода d и y
    d_input = ft.TextField(label="Введите значение для переменной d", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления R
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate_g(d_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(d_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)