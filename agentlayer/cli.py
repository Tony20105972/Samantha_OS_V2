# agentlayer/cli.py

import typer
from agentlayer.flow import run_flow
from agentlayer.rule_checker import check_rules

app = typer.Typer()

@app.command()
def run():
    result = run_flow()
    check_rules(result)

def run_cli():
    app()
