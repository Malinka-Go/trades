import websocket
import json
import mysql.connector

# Подключимся к базе данных
cnx = mysql.connector.connect(host="localhost", user="root", passwd="", db="bin_rec_trd")
cursor = cnx.cursor()

def on_message(ws, message):
    

    data = json.loads(message)  # Выгрузим JSON в массив

    # Переберём массив данных(json)
    for crypto_symbol in data:
        cursor.execute(f"INSERT INTO `smallbin` (`prices`, `quants`) VALUES ('[4]', '[5]') ON DUPLICATE KEY UPDATE price = '[5]';")  # Записать изменение количества

    cnx.commit()  # Зафиксировать транзакции
    

    def on_close(ws):
        print("### closed ###")

    ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/bnbusdt@trade",
                            on_message=on_message,
                            on_close=on_close)

    ws.run_forever()  # Set dispatcher to automatic reconnection