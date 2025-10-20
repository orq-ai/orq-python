"""Dependency validation for OpenAI Agents Instrumentation."""

import importlib
from typing import List, Tuple, Optional


def _check_dependency(package_name: str, pip_name: Optional[str] = None) -> Tuple[bool, str]:
    """
    Check if a dependency is available.
    
    Args:
        package_name: The package name to import
        pip_name: The pip package name (if different from import name)
    
    Returns:
        Tuple of (is_available, pip_package_name)
    """
    pip_package = pip_name or package_name
    try:
        importlib.import_module(package_name)
        return True, pip_package
    except ImportError:
        return False, pip_package


def validate_dependencies() -> None:
    """
    Validate that all required dependencies are installed.
    
    Raises:
        ImportError: If any required dependencies are missing, with installation instructions.
    """
    required_deps = [
        ("agents", "openai-agents"),
        ("opentelemetry.exporter.otlp", "opentelemetry-exporter-otlp"),
        ("opentelemetry.sdk", "opentelemetry-sdk"),
        ("opentelemetry.instrumentation.instrumentor", "opentelemetry-instrumentation")
    ]
    
    missing_deps: List[str] = []
    
    for import_name, pip_name in required_deps:
        is_available, pip_package = _check_dependency(import_name, pip_name)
        if not is_available:
            missing_deps.append(pip_package)
    
    if missing_deps:
        deps_str = " ".join(missing_deps)
        raise ImportError(
            f"Missing required dependencies: {', '.join(missing_deps)}. "
            f"Please install them using: pip install {deps_str}"
        )