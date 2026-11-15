"""Entrena el modelo base (regresión logística sobre WoE) y el retador (LightGBM).

Registra cada corrida en MLflow local: parámetros, métricas y el modelo.
"""


def train_scorecard(X_woe, y):
    """TODO (Fase 2): LogisticRegression sobre variables WoE. Convierte coeficientes a puntos de score."""
    raise NotImplementedError


def train_lightgbm(X, y, X_val, y_val):
    """TODO (Fase 3): LightGBM con early stopping sobre validación. Usa is_unbalance o scale_pos_weight."""
    raise NotImplementedError
