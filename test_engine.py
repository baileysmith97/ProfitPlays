# model.py
# Combines base stats + rule adjustments into final projections

from stats import get_base_projection
from rules import get_rule_adjustments

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
    }
# stats.py
# Statistical engine for base projections using weighted averages

def get_base_projection(sport, stats):
    """
    sport: 'NBA', 'NFL', etc.
    stats: dictionary of raw statistical inputs
    returns: dictionary of base projections before rule adjustments
    """

    if sport == 'NBA':
        return nba_base_projection(stats)
    elif sport == 'NFL':
        return nfl_base_projection(stats)
    else:
        return {}


# -----------------------------
# NBA BASE PROJECTIONS
# -----------------------------
def nba_base_projection(s):
    """
    s = {
        'season_avg_pts': float,
        'last5_avg_pts': float,
        'season_avg_reb': float,
        'last5_avg_reb': float,
        'season_avg_ast': float,
        'last5_avg_ast': float,
        'pace_factor': float,   # multiplier like 0.95 to 1.10
        'usage_factor': float   # multiplier like 0.90 to 1.15
    }
    """

    proj = {}

    # Points projection
    pts = (
        0.45 * s.get('season_avg_pts', 0) +
        0.45 * s.get('last5_avg_pts', 0) +
        0.10 * s.get('season_avg_pts', 0) * s.get('pace_factor', 1)
    )
    pts *= s.get('usage_factor', 1)
    proj['points'] = round(pts, 2)

    # Rebounds projection
    reb = (
        0.50 * s.get('season_avg_reb', 0) +
        0.40 * s.get('last5_avg_reb', 0) +
        0.10 * s.get('season_avg_reb', 0) * s.get('pace_factor', 1)
    )
    proj['rebounds'] = round(reb, 2)

    # Assists projection
    ast = (
        0.50 * s.get('season_avg_ast', 0) +
        0.40 * s.get('last5_avg_ast', 0) +
        0.10 * s.get('season_avg_ast', 0) * s.get('pace_factor', 1)
    )
    proj['assists'] = round(ast, 2)

    return proj

