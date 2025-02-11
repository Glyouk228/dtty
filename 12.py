import flet as ft
import numpy as np

def calculate_g(t_input, y_input, result_text):
    # Получаем значения t и y из текстовых полей
    t = float(t_input.value)
    y = float(y_input.value)
    
    # Вычисляем R
    R = np.sin(np.power((2 * t + 1),2)) + 0.3 / np.log10(t + y)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'R = {R}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №12"
    
    # Создаем текстовые поля для ввода t и y
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления R
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate_g(t_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(t_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)