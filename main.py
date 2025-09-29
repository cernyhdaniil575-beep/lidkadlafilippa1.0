from random import*
symbols = ['🍒', '🍋', '🍊', '🍇', '🔔', '💎']
while True:
    input("Нажмите Enter чтобы крутить слоты...")
    results = choices(symbols, k=3)
    print(f"| {results[0]} | {results[1]} | {results[2]} |")
    if results[0] == results[1] == results[2]:
        print("ДЖЕКПОТ! Вы выиграли!")
    elif results[0] == results[1] or results[1] == results[2]:
        print("Почти! Выпало два одинаковых символа!")
    else:
        print("Повезет в следующий раз!")
