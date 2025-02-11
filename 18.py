import flet as ft
import numpy as np

def calculate_g(k_input, y_input, result_text):
    # Получаем значения k и y из текстовых полей
    k = float(k_input.value)
    y = float(y_input.value)
    
    # Вычисляем R
    R = np.sqrt(np.power(np.sin(y), 2)) + 6.835 / np.log(y + k) + 3 * np.power(y, 2)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'R = {R}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №18"
    
    # Создаем текстовые поля для ввода k и y
    k_input = ft.TextField(label="Введите значение для переменной k", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления R
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate_g(k_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(k_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)