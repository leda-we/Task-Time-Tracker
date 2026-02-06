import questionary
result = questionary.select(
    "Тест:",
    choices=["Работает", "Не работает"],
).unsafe_ask()

print("Результат:", result)