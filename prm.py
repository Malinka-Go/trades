import websocket
import json
import MySQLdb

# Подключимся к базе данных
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="bin_rec_trd")
cursor = db.cursor()

def on_message(ws, message):
    

    data = json.loads(message)  # Выгрузим JSON в массив

    # Переберём массив данных(json)
    for crypto_symbol in data:
        cursor.execute(f"INSERT INTO `smallbin` (`prices`, `quants`) VALUES ('[4]', '[5]') ON DUPLICATE KEY UPDATE price = '[5]';")  # Записать изменение количества

    db.commit()  # Зафиксировать транзакции
    

    def on_close(ws):
        print("### closed ###")

    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/bnbusdt@trade",
                            on_message=on_message,
                            on_close=on_close)

    ws.run_forever()  # Set dispatcher to automatic reconnection