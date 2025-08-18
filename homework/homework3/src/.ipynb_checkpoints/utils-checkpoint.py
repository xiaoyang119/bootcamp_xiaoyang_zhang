def get_summary_stats(df, group_col=None):
    stats = {
        'describe': df.describe(),
        'grouped': df.groupby('category').mean(numeric_only=True).reset_index()
    }
    return stats
