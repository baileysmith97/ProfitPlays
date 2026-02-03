# feature_builder.py
# Builds all required inputs for the model

def build_features(player_data):
    """
    player_data: raw scraped or manually entered data
    returns: stats, ctx, patterns
    """

    stats = player_data.get('stats', {})
    ctx = player_data.get('context', {})
    patterns = player_data.get('patterns', {})

    return stats, ctx, patterns
