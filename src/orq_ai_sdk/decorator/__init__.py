"""Orq Python Decorator SDK for distributed tracing."""

from decorator.decorators import traced
from decorator.types import SpanType

# TODO: review what functions to expose
__all__ = ["traced", "SpanType"]