"""Carga y limpieza del dataset Give Me Some Credit (Kaggle, archivo cs-training.csv).

Variable objetivo: SeriousDlqin2yrs (1 = atraso de 90+ días en los próximos 2 años).
"""
from pathlib import Path

import pandas as pd

TARGET = "SeriousDlqin2yrs"
RAW_PATH = Path("data/raw/cs-training.csv")


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    """Lee el CSV crudo. La primera columna sin nombre es un índice: elimínala."""
    df = pd.read_csv(path)
    return df.drop(columns=[c for c in df.columns if c.startswith("Unnamed")])


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """TODO (Fase 1): decide y documenta en el README cada regla.

    - MonthlyIncome y NumberOfDependents tienen nulos: ¿imputar mediana o crear bandera?
    - Los contadores de atraso tienen valores 96/98 (códigos, no conteos reales).
    - RevolvingUtilizationOfUnsecuredLines y DebtRatio tienen valores extremos.
    - age = 0 es un error de captura.
    """
    raise NotImplementedError


def split(df: pd.DataFrame, seed: int = 42):
    """TODO (Fase 1): train / validación / prueba 60/20/20 estratificado por TARGET.

    La prueba no se toca hasta el final. Eso es lo que te pedirán defender.
    """
    raise NotImplementedError
