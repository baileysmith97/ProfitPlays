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


# -----------------------------
# NFL BASE PROJECTIONS
# -----------------------------
def nfl_base_projection(s):
    """
    s = {
        'season_avg_rush': float,
        'last5_avg_rush': float,
        'season_avg_rec': float,
        'last5_avg_rec': float,
        'season_avg_receptions': float,
        'last5_avg_receptions': float,
        'snap_share_factor': float,   # 0.80 to 1.20
        'target_share_factor': float  # 0.80 to 1.20
    }
    """

    proj = {}

    # Rushing yards
    rush = (
        0.50 * s.get('season_avg_rush', 0) +
        0.40 * s.get('last5_avg_rush', 0)
    )
    rush *= s.get('snap_share_factor', 1)
    proj['rush_yards'] = round(rush, 2)

    # Receiving yards
    rec = (
        0.50 * s.get('season_avg_rec', 0) +
        0.40 * s.get('last5_avg_rec', 0)
    )
    rec *= s.get('target_share_factor', 1)
    proj['rec_yards'] = round(rec, 2)

    # Receptions
    recs = (
        0.50 * s.get('season_avg_receptions', 0) +
        0.40 * s.get('last5_avg_receptions', 0)
    )
    recs *= s.get('target_share_factor', 1)
    proj['receptions'] = round(recs, 2)

    return proj
