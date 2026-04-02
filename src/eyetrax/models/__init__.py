import pkgutil
from importlib import import_module
from typing import Dict, Type

from .base import BaseModel

__all__ = ["BaseModel", "create_model", "AVAILABLE_MODELS"]

AVAILABLE_MODELS: Dict[str, Type[BaseModel]] = {}


def register_model(name: str, cls: Type[BaseModel]) -> None:
    if name in AVAILABLE_MODELS:
        raise ValueError(f"Model name '{name}' already registered")
    AVAILABLE_MODELS[name] = cls


def _auto_discover() -> None:
    for _, mod_name, _ in pkgutil.iter_modules(__path__):
        if mod_name == "base":
            continue
        import_module(f"{__name__}.{mod_name}")


def create_model(name: str, **kwargs) -> BaseModel:
    if not AVAILABLE_MODELS:
        _auto_discover()
    try:
        cls = AVAILABLE_MODELS[name]
    except KeyError as e:
        raise ValueError(
            f"Unknown model '{name}'. Available: {sorted(AVAILABLE_MODELS)}"
        ) from e
    return cls(**kwargs)
