from model import run_model
from patterns import detect_patterns
from feature_builder import build_features

# Simulated player data
player_data = {
    'name': 'Jalen Brunson',
    'sport': 'NBA',
    'stats': {
        'season_avg_pts': 24.5,
        'last5_avg_pts': 29.0,
        'season_avg_reb': 3.8,
        'last5_avg_reb': 4.2,
        'season_avg_ast': 6.1,
        'last5_avg_ast': 6.8,
        'pace_factor': 1.04,
        'usage_factor': 1.10
    },
    'context': {
        'pace_diff': 5,
        'usage_change': 0.06,
        'minutes_proj': 38,
        'opp_vs_position_rank': 27,
        'is_home': True,
        'teammate_out_starter': True
    },
    'patterns': {
        'last5_pts_avg': 29.0,
        'season_pts_avg': 24.5,
        'last3_min_avg': 37.5,
        'season_min_avg': 33.0
    }
}

# Build features
stats, ctx, pattern_inputs = build_features(player_data)

# Detect patterns
signals = detect_patterns(player_data['sport'], pattern_inputs)
print("Pattern Signals:", signals)

# Run full model
output = run_model(player_data['sport'], stats, ctx)
print("Base Projection:", output['base'])
print("Rule Adjustments:", output['rules'])
print("Final Projection:", output['final'])# model.py
# Combines base stats + rule adjustments into final projections

from stats import get_base_projection
from rules import get_rule_adjustments# patterns.py
# Detects trends and role changes

def detect_patterns(sport, data):
    """
    data: dictionary of recent game logs or usage trends
    returns: dictionary of pattern signals
    """

    signals = {}

    # Hot streak detection
    if data.get('last5_pts_avg', 0) - data.get('season_pts_avg', 0) >= 4:
        signals['hot_streak'] = True
    else:
        signals['hot_streak'] = False

    # Cold streak detection
    if data.get('season_pts_avg', 0) - data.get('last5_pts_avg', 0) >= 4:
        signals['cold_streak'] = True
    else:
        signals['cold_streak'] = False

    # Role change (minutes spike)
    if data.get('last3_min_avg', 0) - data.get('season_min_avg', 0) >= 4:
        signals['role_increase'] = True
    else:
        signals['role_increase'] = False

    return signals

def run_model(sport, stats, ctx):
    """
    sport: 'NBA' or 'NFL'
    stats: dictionary of statistical inputs
    ctx: dictionary of contextual inputs
    """
    base = get_base_projection(sport, stats)
    rules = get_rule_adjustments(sport, ctx)

    final = {k: base.get(k, 0) + rules.get(k, 0) for k in base}
    return {
        'base': base,
        'rules': rules,
        'final': final
    }# scanner.py
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
