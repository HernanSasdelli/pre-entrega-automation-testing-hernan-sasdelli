import os
import logging


def configurar_logger(log_path: str) -> logging.Logger:
    """
    Configura un logger único para toda la suite.
    """
    logger = logging.getLogger("suite")
    logger.setLevel(logging.INFO)

    # evita duplicar headles
    
    if logger.handlers:
        return logger

    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    return logger
