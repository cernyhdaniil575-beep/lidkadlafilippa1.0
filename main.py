from random import*
balans_user=float(input('сколько дэпнешь?'))
balans_user1=balans_user
def slot_fryuts(balans):
    symbols = ['🍒', '🍋', '🍊', '🍇', '🔔', '💎']
    while True:
        stavka=(input('введите ставку'))
        if stavka=='':
            print('eblan vvedi chislo')
            print(balans)
            break
        stavka=int(stavka)
        if stavka==0:
            break
        while balans-stavka>=0:
            input("Нажмите Enter чтобы крутить слоты...")
            results = choices(symbols, k=5)
            print(f" {results[0]}  {results[1]}  {results[2]} {results[3]}  {results[4]} ")
            results2 = choices(symbols, k=5)
            print(f" {results2[0]}  {results2[1]}  {results2[2]} {results2[3]}  {results2[4]} ")
            results3 = choices(symbols, k=5)
            print(f" {results3[0]}  {results3[1]}  {results3[2]} {results3[3]}  {results3[4]} ")
            results4 = choices(symbols, k=5)
            print(f" {results4[0]}  {results4[1]}  {results4[2]} {results4[3]}  {results4[4]} ")
            if results[0] == results[1]==results[2]==results[3] == results[4]:
                print("ДЖЕКПОТ! Вы выиграли!",stavka*100)
                balans+=stavka*100
            elif results2[0] == results2[1]==results2[2]==results2[3] == results2[4]:
                print("ДЖЕКПОТ! Вы выиграли!",stavka*100)
                balans+=stavka*100
            elif results3[0] == results3[1] == results3[2] == results3[3] == results3[4]:
                print("ДЖЕКПОТ! Вы выиграли:",stavka*100)
                balans += stavka * 100
            elif results4[0] == results4[1] == results4[2] == results4[3] == results4[4]:
                print("ДЖЕКПОТ! Вы выиграли!",stavka*100)
                balans += stavka * 100
            elif results[0]==results2[1]==results3[2]==results2[3]==results[4]:
                print('УДАЧА! ВАШ ВЫИГРЫШ:',stavka*10)
                balans += stavka * 10
            elif results2[0]==results3[1]==results4[2]==results3[3]==results2[4]:
                print('УДАЧА! ВАШ ВЫИГРЫШ:',stavka*10)
                balans += stavka*10
            elif results4[0]==results3[1]==results2[2]==results3[3]==results4[4]:
                print('УДАЧА! ВАШ ВЫИГРЫШ:',stavka*10)
                balans += stavka * 10
            elif results3[0]==results2[1]== results[2] ==results2[3]==results3[4]:
                print('УДАЧА! ВАШ ВЫИГРЫШ:',stavka*10)
                balans += stavka * 10
            else:
                print("Повезет в следующий раз!")
            print(f'ваш текущий баланс:',balans-stavka)
            game=input('играем дальше?')
            balans=balans-stavka
            balans_user1=balans
            if game=='нет' or game=='no':
                break
            if balans-stavka<0:
                print('пополните баланс или понизьте ставку')
                break
slot_fryuts(balans_user1)
