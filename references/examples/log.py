from obs_metrics.logger import Logger
from obs_metrics.config import config

logger = Logger(service_name="payment-service")

logger.info("Serviço aprovado", context={"pedido": 123})
logger.error("Erro na transação", context={"erro": "timeout", "usuario_id": 456})