import flet as ft
import numpy as np

def calculate_g(w_input, y_input, result_text):
    # Получаем значения w и y из текстовых полей
    w = float(w_input.value)
    y = float(y_input.value)
    
    # Вычисляем G
    G = 9.33 * np.power(w, 3) + np.sqrt(w) / np.log10(y + 3.5) + np.sqrt(y)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'G = {G}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №4"
    
    # Создаем текстовые поля для ввода w и y
    w_input = ft.TextField(label="Введите значение для переменной w", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления G
    calculate_button = ft.ElevatedButton(text="Вычислить G", on_click=lambda e: calculate_g(w_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(w_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)