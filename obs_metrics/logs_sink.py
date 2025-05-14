import json
import asyncio
import requests
from requests.auth import HTTPBasicAuth

import aiohttp

from .config import config

def send_log(log_data):
    """
    Send log data to ElasticSearch.
    
    Args:
        log_data (dict): The log data to send.
    """
    if config.ASYNC_SEND:
        # Rodar em thread loop se estiver em contexto sync  
        try:
            asyncio.get_running_loop()
            asyncio.create_task(_send_log_async(log_data))
        except RuntimeError:
            asyncio.run(_send_log_async(log_data))
    else:
        _send_log(log_data)

def _send_log(log_data):
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            f"{config.ELASTIC_URL}/logs/_doc",
            headers=headers,
            data=json.dumps(log_data),
            auth=HTTPBasicAuth(config.ELASTIC_USER, config.ELASTIC_PASSWORD),
            timeout=2
        )
        response.raise_for_status()
        print('Sended log to ElasticSearch:', response.status_code)
    except Exception as e:
        print("Erro ao enviar log (sync):", e)
        
async def _send_log_async(log_data):
    """
    Send log data to ElasticSearch asynchronously.
    
    Args:
        log_data (dict): The log data to send.
    """
    try:
        headers = {"Content-Type": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{config.ELASTIC_URL}/logs/_doc",
                headers=headers,
                json=log_data,
                auth=aiohttp.BasicAuth(config.ELASTIC_USER, config.ELASTIC_PASSWORD)
            ) as response:
                if response.status not in {200, 201}:
                    print('Error sending log to ElasticSearch:', response.status)
    except Exception as e:
        print("Erro ao enviar log (async):", e)