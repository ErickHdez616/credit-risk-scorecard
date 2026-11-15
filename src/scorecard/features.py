"""Binning y Weight of Evidence (WoE) para el scorecard.

WoE de un bin = ln(% de buenos en el bin / % de malos en el bin).
Information Value (IV) = suma de (%buenos - %malos) * WoE. Regla común:
IV < 0.02 inútil, 0.02-0.1 débil, 0.1-0.3 medio, > 0.3 fuerte.
"""
import pandas as pd


def fit_bins(X: pd.DataFrame, y: pd.Series, n_bins: int = 5) -> dict:
    """TODO (Fase 2): bins por cuantiles en train; guarda los cortes para aplicarlos igual en prueba."""
    raise NotImplementedError


def woe_transform(X: pd.DataFrame, bins: dict) -> pd.DataFrame:
    """TODO (Fase 2): reemplaza cada valor por el WoE de su bin."""
    raise NotImplementedError


def information_value(X: pd.DataFrame, y: pd.Series, bins: dict) -> pd.Series:
    """TODO (Fase 2): IV por variable, ordenado de mayor a menor."""
    raise NotImplementedError
