"""Métricas que usa riesgo de crédito.

- AUC: capacidad de ordenar buenos vs malos.
- Gini = 2 * AUC - 1 (la métrica que más verás en banca).
- KS: máxima separación entre las distribuciones acumuladas de buenos y malos.
- Calibración: ¿una PD de 10 % significa 10 % de impagos reales?
"""
import numpy as np
from sklearn.metrics import roc_auc_score


def gini(y_true, y_score) -> float:
    return 2 * roc_auc_score(y_true, y_score) - 1


def ks(y_true, y_score) -> float:
    """TODO (Fase 3): KS con las curvas acumuladas de buenos y malos."""
    raise NotImplementedError


def best_threshold_by_cost(y_true, y_score, cost_fn: float = 5.0, cost_fp: float = 1.0) -> float:
    """TODO (Fase 3): umbral que minimiza costo esperado.

    cost_fn = costo de aprobar a alguien que no paga. cost_fp = costo de rechazar a alguien bueno.
    Documenta en el README por qué elegiste esos costos.
    """
    raise NotImplementedError


def calibration_table(y_true, y_score, n_bins: int = 10):
    """TODO (Fase 3): PD promedio predicha vs tasa real por decil."""
    raise NotImplementedError
