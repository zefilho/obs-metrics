import os
import logging
from dotenv import load_dotenv
from typing import Dict, Any
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

@dataclass
class Config:
    ELASTIC_URL: str = field(default="http://localhost:9200")
    ELASTIC_USER: str = field(default="elastic")
    ELASTIC_PASSWORD: str = field(default="admin123")
    SERVICE_NAME: str = field(default="default-service")
    ENVIRONMENT: str = field(default="development")
    ASYNC_SEND: bool = field(default=False)
    
    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        self._validate_config()
    
    @classmethod
    def get(cls, path_env: str = '.env') -> 'Config':
        """
        Create a Config instance from environment variables.
        parm:
            path_env: Path to .env
        Returns:
            Config: A populated configuration object
        """

        """Load environment variables from a .env file."""
        if os.path.exists(path_env):
            load_dotenv(path_env)
            logging.info(f"Environment variables loaded from {path_env}")
        else:
            logging.warning(f"Environment file {path_env} does not exist.")
        
        raw_values = {
            "ELASTIC_URL": os.getenv("ELASTIC_URL"),
            "ELASTIC_USER": os.getenv("ELASTIC_USER"),
            "ELASTIC_PASSWORD": os.getenv("ELASTIC_PASSWORD"),
            "SERVICE_NAME": os.getenv("SERVICE_NAME"),
            "ENVIRONMENT": os.getenv("ENVIRONMENT"),
            "ASYNC_SEND": os.getenv("ASYNC_SEND")
        }
        
        # Filter out None values to avoid overriding defaults
        filtered_values = {k: v for k, v in raw_values.items() if v is not None}
        
        # Convert ASYNC_SEND string to boolean
        if "ASYNC_SEND" in filtered_values:
            filtered_values["ASYNC_SEND"] = filtered_values["ASYNC_SEND"].lower() == "true"
        
        # Create instance with values from environment
        config = cls(**filtered_values)
        config._raw_values = raw_values
        
        return config
    
    def _validate_config(self) -> None:
        """Validate configuration values."""
        # Validate ELASTIC_URL
        if not self.ELASTIC_URL.startswith(("http://", "https://")):
            logger.warning(f"ELASTIC_URL does not start with http:// or https://: {self.ELASTIC_URL}")
        
        # Validate ENVIRONMENT
        valid_environments = {"development", "staging", "production", "testing"}
        if self.ENVIRONMENT not in valid_environments:
            logger.warning(
                f"ENVIRONMENT '{self.ENVIRONMENT}' is not one of {valid_environments}. "
                "This might cause unexpected behavior."
            )
    
    def as_dict(self) -> Dict[str, Any]:
        return {
            "ELASTIC_URL": self.ELASTIC_URL,
            "SERVICE_NAME": self.SERVICE_NAME,
            "ENVIRONMENT": self.ENVIRONMENT,
            "ASYNC_SEND": self.ASYNC_SEND,
        }
    

# Default configuration instance for import
config = Config.get()

if __name__ == "__main__":
    # Example usage
    print(f"Loaded configuration: {config}")
    print(f"As dictionary: {config.as_dict()}")
    
    # Access individual settings
    print(f"ENVIRONMENT: {config.ENVIRONMENT}")
    print(f"ASYNC_SEND: {config.ASYNC_SEND} (type: {type(config.ASYNC_SEND).__name__})")
