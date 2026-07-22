"""
Lê os 10 arquivos JSON de issues fake (pasta issues_fake/, um arquivo por
issue) e imprime somente as issues com prioridade Blocker ou Critical,
ordenadas por id.

Definição:
- Blocker: impede totalmente o progresso (build quebrado, sistema não sobe,
  ninguém consegue testar/trabalhar até resolver).
- Critical: função essencial quebrada ou sistema instável, mas ainda dá pra
  contornar ou trabalhar em outras partes.
"""

import json
from pathlib import Path

PASTA_ISSUES = Path(__file__).parent / "issues_fake"
PRIORIDADES_ALVO = {"Blocker", "Critical"}


def carregar_issues(pasta: Path) -> list[dict]:
    issues = []
    for arquivo in sorted(pasta.glob("*.json")):
        with open(arquivo, "r", encoding="utf-8") as f:
            issues.append(json.load(f))
    return issues


def filtrar_e_ordenar(issues: list[dict]) -> list[dict]:
    filtradas = [i for i in issues if i["prioridade"] in PRIORIDADES_ALVO]
    return sorted(filtradas, key=lambda i: i["id"])


def imprimir_issues(issues: list[dict]) -> None:
    if not issues:
        print("Nenhuma issue Blocker/Critical encontrada.")
        return

    for issue in issues:
        print(f"[#{issue['id']}] ({issue['prioridade']}) {issue['titulo']}")
        print(f"    {issue['descricao']}")
        print()


def main() -> None:
    issues = carregar_issues(PASTA_ISSUES)
    relevantes = filtrar_e_ordenar(issues)
    imprimir_issues(relevantes)


if __name__ == "__main__":
    main()
