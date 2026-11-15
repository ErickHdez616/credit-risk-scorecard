"""Explicabilidad: SHAP decide los motivos; Claude solo los redacta.

Regla de diseño: Claude nunca recibe la decisión para cambiarla ni calcula nada.
Recibe la PD, el resultado y los 3 motivos SHAP, y devuelve una carta en lenguaje claro.
"""
import os

from pydantic import BaseModel


class Reason(BaseModel):
    feature: str
    value: float
    shap_value: float


def top_reasons(model, x_row, n: int = 3) -> list[Reason]:
    """TODO (Fase 4): shap.TreeExplainer(model); devuelve las n variables que más empujan hacia impago."""
    raise NotImplementedError


def draft_letter(pd_value: float, approved: bool, reasons: list[Reason]) -> str:
    """TODO (Fase 4): una llamada a la API de Claude con el SDK `anthropic`.

    - Modelo: os.environ["CLAUDE_MODEL"] (Haiku 5.5 por defecto).
    - System prompt: no inventes motivos, usa solo los recibidos, no prometas nada, español claro.
    - Valida que la carta mencione los 3 motivos (un test en tests/).
    """
    raise NotImplementedError
