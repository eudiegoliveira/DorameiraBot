import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Token de acesso a API do Telegram
TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")
if not TOKEN_TELEGRAM:
    logging.error("Erro: TOKEN_TELEGRAM não encontrado nas \
        variáveis de ambiente ou no arquivo .env")
    raise ValueError("Token do Telegram não configurado. \
        Verifique as variáveis de ambiente ou o arquivo .env")

# Token de acesso a API do MercadoPago
TOKEN_MERCADOPAGO = os.getenv("TOKEN_MERCADOPAGO")
if not TOKEN_MERCADOPAGO:
    logging.error("Erro: TOKEN_MERCADOPAGO não encontrado nas \
        variáveis de ambiente ou no arquivo .env")
    raise ValueError("Token do MercadoPago não configurado. \
        Verifique as variáveis de ambiente ou o arquivo .env")

# ID dono do bot (vai ser usado para enviar notificação)
OWNER_ID = os.getenv("OWNER_ID")