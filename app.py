from flask import Flask, render_template, request, jsonify
from random import choices
import json

app = Flask(__name__)

# Глобальная переменная для хранения состояния игры
game_state = {
    'balance': 1000.0,  # Начальный баланс
    'current_bet': 0,
    'game_active': False
}

def check_win(results):
    """Проверяет выигрышные комбинации"""
    # Проверка на джекпот (5 одинаковых символов в ряду)
    for row in results:
        if len(set(row)) == 1:
            return 'jackpot', 100
    
    # Проверка диагональных комбинаций
    diagonal1 = [results[0][0], results[1][1], results[2][2], results[3][3], results[4][4]]
    diagonal2 = [results[0][4], results[1][3], results[2][2], results[3][1], results[4][0]]
    
    if len(set(diagonal1)) == 1:
        return 'diagonal', 10
    if len(set(diagonal2)) == 1:
        return 'diagonal', 10
    
    return 'lose', 0

@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html')

@app.route('/api/balance')
def get_balance():
    """Получить текущий баланс"""
    return jsonify({'balance': game_state['balance']})

@app.route('/api/set_balance', methods=['POST'])
def set_balance():
    """Установить новый баланс"""
    data = request.get_json()
    new_balance = float(data.get('balance', 1000))
    game_state['balance'] = new_balance
    game_state['game_active'] = True
    return jsonify({'success': True, 'balance': game_state['balance']})

@app.route('/api/spin', methods=['POST'])
def spin():
    """Крутить слоты"""
    data = request.get_json()
    bet = float(data.get('bet', 0))
    
    if bet <= 0 or bet > game_state['balance']:
        return jsonify({'error': 'Неверная ставка'}), 400
    
    # Вычитаем ставку
    game_state['balance'] -= bet
    game_state['current_bet'] = bet
    
    # Генерируем результаты
    symbols = ['🍒', '🍋', '🍊', '🍇', '🔔', '💎']
    results = []
    for _ in range(5):
        row = choices(symbols, k=5)
        results.append(row)
    
    # Проверяем выигрыш
    win_type, multiplier = check_win(results)
    
    if win_type != 'lose':
        winnings = bet * multiplier
        game_state['balance'] += winnings
        message = f"Поздравляем! Вы выиграли {winnings:.2f}!"
        if win_type == 'jackpot':
            message = f"ДЖЕКПОТ! Вы выиграли {winnings:.2f}!"
        elif win_type == 'diagonal':
            message = f"УДАЧА! ВАШ ВЫИГРЫШ: {winnings:.2f}!"
    else:
        message = "Повезет в следующий раз!"
    
    return jsonify({
        'success': True,
        'results': results,
        'balance': game_state['balance'],
        'win_type': win_type,
        'winnings': bet * multiplier if win_type != 'lose' else 0,
        'message': message
    })

@app.route('/api/reset', methods=['POST'])
def reset_game():
    """Сбросить игру"""
    game_state['balance'] = 1000.0
    game_state['current_bet'] = 0
    game_state['game_active'] = False
    return jsonify({'success': True, 'balance': game_state['balance']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
