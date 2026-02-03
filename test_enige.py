# rules.py
# Core rule-based adjustment engine for all sports

def get_rule_adjustments(sport, ctx):
    """
    sport: string ('NBA', 'NFL', etc.)
    ctx: dictionary containing player/game context
    returns: dictionary of stat adjustments
    """
    if sport == 'NBA':
        return nba_rules(ctx)
    elif sport == 'NFL':
        return nfl_rules(ctx)
    else:
        return {}


# -----------------------------
# NBA RULES
# -----------------------------
def nba_rules(ctx):
    adj = {'points': 0.0, 'rebounds': 0.0, 'assists': 0.0}

    # Pace adjustment
    if ctx.get('pace_diff', 0) >= 5:
        adj['points'] += 1.5
    elif ctx.get('pace_diff', 0) <= -5:
        adj['points'] -= 1.5

    # Usage change
    if ctx.get('usage_change', 0) >= 0.05:
        adj['points'] += 2.0
        adj['assists'] += 0.5

    # Minutes projection
    if ctx.get('minutes_proj', 0) >= 36:
        adj['points'] += 1.0
        adj['rebounds'] += 0.5

    # Opponent vs position
