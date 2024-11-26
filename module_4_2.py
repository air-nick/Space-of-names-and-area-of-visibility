# Создаем основную функцию test_function
def test_function():
    # Создаем вложенную функцию inner_function
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызываем функцию inner_function внутри test_function
    inner_function()


# Вызываем функцию test_function
test_function()

# Попробуем вызвать inner_function вне функции test_function
# inner_function()  # Этот вызов приведет к ошибке NameError, так как inner_function не видна за пределами test_function
