# patterns.py
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
