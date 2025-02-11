import flet as ft
import numpy as np

def calculate_g(a_input, y_input, t_input, result_text):
    # Получаем значения a и y и t из текстовых полей
    a = float(a_input.value)
    y = float(y_input.value)
    t = float(t_input.value)
    
    # Вычисляем D
    D = 7.8 * np.power(a, 2) + 3.52 * t / np.log10(a + 2 * y) + np.exp(y)
    
    # Обновляем текстовое поле с результатом 
    result_text.value =f'D = {D}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №5"
    
    # Создаем текстовые поля для ввода a и y и t
    a_input = ft.TextField(label="Введите значение для переменной a", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)
    
    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления D
    calculate_button = ft.ElevatedButton(text="Вычислить D", on_click=lambda e: calculate_g(a_input, y_input, t_input, result_text))

    # Добавляем элементы на страницу
    page.add(a_input, y_input, t_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)