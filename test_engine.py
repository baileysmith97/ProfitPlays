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
print("Final Projection:", output['final'])
