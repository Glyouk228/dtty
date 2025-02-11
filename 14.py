import flet as ft
import numpy as np

def calculate_g(h_input, y_input, result_text):
    # Получаем значения h и y из текстовых полей
    h = float(h_input.value)
    y = float(y_input.value)
    
    # Вычисляем P
    P = np.exp(y + 2.5) + 7.7 * np.power(h, 3) / np.log(np.sqrt(y + 0.004 * h))
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'P = {P}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №14"
    
    # Создаем текстовые поля для ввода h и y
    h_input = ft.TextField(label="Введите значение для переменной h", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления P
    calculate_button = ft.ElevatedButton(text="Вычислить P", on_click=lambda e: calculate_g(h_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(h_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)