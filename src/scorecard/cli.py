"""CLI: `score train`, `score evaluate`, `score predict solicitud.json --explain`."""
import typer

app = typer.Typer(help="Modelo de probabilidad de impago explicable.")


@app.command()
def train():
    """Entrena scorecard y LightGBM y los registra en MLflow."""
    raise NotImplementedError("Fase 2-3")


@app.command()
def evaluate():
    """Imprime AUC, Gini, KS y calibración de ambos modelos sobre el set de prueba."""
    raise NotImplementedError("Fase 3")


@app.command()
def predict(path: str, explain: bool = typer.Option(False, "--explain")):
    """Calcula la PD de una solicitud en JSON; con --explain añade motivos SHAP y la carta de Claude."""
    raise NotImplementedError("Fase 4")


if __name__ == "__main__":
    app()
