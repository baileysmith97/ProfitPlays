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
