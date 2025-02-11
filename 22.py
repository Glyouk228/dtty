import flet as ft
import numpy as np

def calculate_g(t_input, y_input, result_text):
    # Получаем значения t и y из текстовых полей
    t = float(t_input.value)
    y = float(y_input.value)
    
    # Вычисляем S
    S = 4.351 * np.power(y, 3) + 2 * t * np.log10(t) / np.sqrt(np.cos(2 * y)) + 4.351
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'S = {S}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №22"
    
    # Создаем текстовые поля для ввода t и y
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления S
    calculate_button = ft.ElevatedButton(text="Вычислить S", on_click=lambda e: calculate_g(t_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(t_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)