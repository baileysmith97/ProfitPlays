# scanner.py
# Scans multiple players and returns edges

from model import run_model

def scan_players(players):
    """
    players: list of dictionaries, each containing:
        - sport
        - stats
        - ctx
        - name
    """

    results = []

    for p in players:
        output = run_model(p['sport'], p['stats'], p['ctx'])
        results.append({
            'name': p['name'],
            'final': output['final'],
            'base': output['base'],
            'rules': output['rules']
        })

    return results
