import flet as ft
import numpy as np

def calculate_g(k_input, y_input, result_text):
    # Получаем значения k и y из текстовых полей
    k = float(k_input.value)
    y = float(y_input.value)
    
    # Вычисляем U
    U = np.log10( k - y) + np.power(y,4) / np.exp(y) + 2.355 * np.power(k,2)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'U = {U}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №3"
    
    # Создаем текстовые поля для ввода k и y
    k_input = ft.TextField(label="Введите значение для переменной k", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления U
    calculate_button = ft.ElevatedButton(text="Вычислить U", on_click=lambda e: calculate_g(k_input, y_input, result_text))

    # Добавляем элементы на страницу
    page.add(k_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)