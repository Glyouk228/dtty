import flet as ft
import numpy as np

def calculate_g(h_input, e_input, y_input, result_text):
    # Получаем значения h и y и e из текстовых полей
    h = float(h_input.value)
    y = float(y_input.value)
    e = float(e_input.value)
    
    # Вычисляем A
    A = np.sin(2 * y + h) + np.power(h,2) / np.power(e , h) + y
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'A = {A}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №13"
    
    # Создаем текстовые поля для ввода h и y и e
    h_input = ft.TextField(label="Введите значение для переменной h", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    e_input = ft.TextField(label="Введите значение для переменной e", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления A
    calculate_button = ft.ElevatedButton(text="Вычислить A", on_click=lambda e: calculate_g(h_input, e_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(h_input, e_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)