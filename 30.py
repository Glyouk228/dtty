import flet as ft
import numpy as np

def calculate_g(p_input, y_input, e_input, result_text):
    # Получаем значения p и y и e из текстовых полей
    p = float(p_input.value)
    y = float(y_input.value)
    e = float(e_input.value)
    
    # Вычисляем N
    N = 3 * np.power(y,2) + np.sqrt(y) + 1 / np.log10(p + y) + np.power(e,p)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'N = {N}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №30"
    
    # Создаем текстовые поля для ввода p и y и e
    p_input = ft.TextField(label="Введите значение для переменной p", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    e_input = ft.TextField(label="Введите значение для переменной e", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления N
    calculate_button = ft.ElevatedButton(text="Вычислить N", on_click=lambda e: calculate_g(p_input, y_input, e_input, result_text))

    # Добавляем элементы на страницу
    page.add(p_input, y_input, e_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)