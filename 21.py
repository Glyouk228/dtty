import flet as ft
import numpy as np

def calculate_g(k_input, p_input, x_input, d_input, result_text):
    # Получаем значения d и x и p и k из текстовых полей
    d = float(d_input.value)
    k = float(k_input.value)
    p = float(p_input.value)
    x = float(x_input.value)
    
    # Вычисляем Q
    Q = np.sqrt(k + 2.6 * p * np.sin(k)) / x - np.power(d , 3)

    # Обновляем текстовое поле с результатом 
    result_text.value =f'Q = {Q}'
    result_text.update()
    
def main(page: ft.Page):
    page.title = "Задание №21"
    
    # Создаем текстовые поля для ввода d и x и p и k
    d_input = ft.TextField(label="Введите значение для переменной d", width=200)
    k_input = ft.TextField(label="Введите значение для переменной k", width=200)
    p_input = ft.TextField(label="Введите значение для переменной p", width=200)
    x_input = ft.TextField(label="Введите значение для переменной x", width=200)

    # Текстовое поле для отображения результата
    result_text = ft.Text(value="", size=20)  
    
    # Кнопка для вычисления Q
    calculate_button = ft.ElevatedButton(text="Вычислить Q", on_click=lambda e: calculate_g(k_input, p_input, x_input, d_input, result_text))

    # Добавляем элементы на страницу
    page.add(k_input, p_input, x_input, d_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)