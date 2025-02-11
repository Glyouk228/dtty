import flet as ft
import numpy as np

def calculate_g(t_input, y_input, result_text):
    # Получаем значения t и y из текстовых полей
    t = float(t_input.value)
    y = float(y_input.value)
    
    # Вычисляем Z
    Z = 2 * t + y * np.cos(t) / np.sqrt(y + 4.831)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'Z = {Z}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №10"
    
    # Создаем текстовые поля для ввода t и y
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления Z
    calculate_button = ft.ElevatedButton(text="Вычислить Z", on_click=lambda e: calculate_g(t_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(t_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)