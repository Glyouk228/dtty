import flet as ft
import numpy as np

def calculate_g(h_input, y_input, e_input, result_text):
    # Получаем значения h и y и e из текстовых полей
    h = float(h_input.value)
    y = float(y_input.value)
    e = float(e_input.value)
    
    # Вычисляем T
    T = 0.355 * np.power(h,2) - 4.355 / np.power(e , y + h) + np.sqrt(2.7 * y)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'T = {T}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №29"
    
    # Создаем текстовые поля для ввода h и y и e
    h_input = ft.TextField(label="Введите значение для переменной h", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    e_input = ft.TextField(label="Введите значение для переменной e", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления T
    calculate_button = ft.ElevatedButton(text="Вычислить T", on_click=lambda e: calculate_g(h_input, y_input, e_input, result_text))

    # Добавляем элементы на страницу
    page.add(h_input, y_input, e_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)