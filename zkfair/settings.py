

# ===================================== options ===================================== #

#----main-options----#
module = 3                                                          # 1 - свап ZKF to USDC, 2 - бридж через орбитер, 3 - отправить USDC на адрес
shuffle = True                                                      # True / False. если нужно перемешать кошельки

decimal_places = 7                                                  # количество знаков, после запятой для генерации случайных чисел

delay_wallets = [10, 20]                                            # минимальная и максимальная задержка между кошельками
delay_transactions = [10, 15]                                       # минимальная и максимальная задержка между транзакциями
waiting_gas = 100                                                   # макс значение газа при котором будет работать скрипт
RETRY_COUNT = 2                                                     # кол-во попыток при возникновении ошибок

#------bot-options------#
bot_status = False                                                  # True / False
bot_token  = ''                                                     # telegram bot token
bot_id     = 0                                                      # telegram id

# =================================== end-options =================================== #


