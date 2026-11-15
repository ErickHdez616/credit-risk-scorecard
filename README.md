# credit-risk-scorecard

Modelo de probabilidad de impago (PD) explicable. Compara un scorecard clásico de banca (regresión logística sobre WoE) contra LightGBM, elige el umbral por costo de negocio, explica cada resultado con SHAP y usa Claude solo para redactar la carta de motivos al cliente.

> Regla de diseño: el modelo predice, SHAP explica, Claude redacta. Claude nunca decide ni calcula.

## Arquitectura

```
cs-training.csv ─► data.py (limpieza, split 60/20/20)
                     ├─► features.py (bins + WoE + IV) ─► train.py: scorecard logístico
                     └─► train.py: LightGBM
                              │
                     evaluate.py (AUC, Gini, KS, calibración, umbral por costo) ─► MLflow
                              │
cli.py `score predict --explain` ─► explain.py: SHAP top 3 ─► Claude (Haiku 5.5) ─► carta
```

## Plan de construcción (16 al 29 nov 2026)

| Fase | Fechas | Qué haces | Entregable | Qué debes poder explicar |
|---|---|---|---|---|
| 0 | 16 nov | Crear el repo, venv, `pip install -e ".[dev]"`, bajar el CSV | `pytest` pasa | Por qué `src/` y no todo en notebooks |
| 1 | 17-18 nov | EDA en `notebooks/01_eda.ipynb`, luego `data.clean()` y `data.split()` | Tabla de reglas de limpieza en este README | Desbalance (~7 % de malos), nulos, códigos 96/98 |
| 2 | 19-21 nov | `features.py` (WoE, IV) y `train_scorecard()` | IV por variable y scorecard en puntos | Qué es WoE e IV y por qué la banca usa scorecards |
| 3 | 22-24 nov | `train_lightgbm()` y `evaluate.py` | Tabla comparativa AUC/Gini/KS de ambos modelos | Por qué no usar accuracy; cómo elegiste el umbral |
| 4 | 25-27 nov | `explain.py`: SHAP y la carta con Claude | `score predict ejemplo.json --explain` funciona | Por qué Claude solo redacta; cómo evitas que invente motivos |
| 5 | 28-29 nov | Drift con Evidently entre dos periodos simulados y README final | Reporte HTML en `reports/` y README con resultados | Qué es drift y cuándo reentrenar |

Después: pausa del 1 al 9 dic por la titulación. P3 (desplegar este modelo en Cloud Run) usa este repo tal cual.

## Datos

- Kaggle, competencia "Give Me Some Credit": archivo `cs-training.csv` en `data/raw/`. Necesitas cuenta de Kaggle y aceptar las reglas de la competencia.
- Alternativa sin Kaggle: la librería `empulse` tiene `empulse.datasets.load_give_me_some_credit()`. Verifica que trae las mismas columnas.
- `data/raw/` está en `.gitignore`: no subas el dataset al repo.

## Cómo correrlo

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # pon tu ANTHROPIC_API_KEY
pytest
score train && score evaluate
score predict ejemplo.json --explain
```

## Resultados

Pendiente: llena esta sección al terminar la Fase 3 con la tabla real de métricas.

## Costo

Cómputo local o Google Colab: 0 MXN. Cartas con Claude Haiku 5.5: centavos de dólar por cientos de cartas.
