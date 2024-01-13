import websocket
import json
import MySQLdb

def on_message(ws, message):
    data = json.loads(message)  # Выгрузим JSON в массив
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="bin_rec_trd") # Подключимся к базе данных
    cursor = db.cursor()
    # Переберём массив данных(json)
    for crypto_symbol in data:
        cursor.execute(f"INSERT INTO `smallbin` (`prices`, `quants`) VALUES ('{crypto_symbol['p']}', '{crypto_symbol['q']}') ON DUPLICATE KEY UPDATE quants = '{crypto_symbol['q']}';")  # Записать изменение количества

    db.commit()  # Зафиксировать транзакции
    db.close() # Закрыть БД

def on_close(ws):
    print("### closed ###")

ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/waxpusdt@trade",
                            on_message=on_message,
                            on_close=on_close)

ws.run_forever()  # Set dispatcher to automatic reconnection