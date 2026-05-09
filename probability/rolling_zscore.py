"""  
## 8. Rolling Z-Score Anomaly Detection — Medium

Given a DataFrame with columns `timestamp`, `sensor_id`, `value`, detect anomalies defined as any reading where the value deviates more than `z` standard deviations from the rolling mean of the **previous** `w` observations for that sensor (excluding the current point).

**Input:** `df`, `w=20`, `z=3.0`
**Output:** Same DataFrame with an added boolean column `is_anomaly`

**Constraint:** No loops over rows. Must handle sensors with fewer than `w` prior observations (mark as non-anomalous until enough history exists).

**What they're testing:** `groupby` + `shift(1)` to avoid look-ahead leakage, `rolling(w).mean()` and `.std()` with `min_periods`, vectorised z-score computation. The shift(1) detail is the trap — most candidates compute rolling stats including the current point, which is data leakage.

"""
import pandas as pd
import numpy as np
# Sample DataFrame
data = {
    'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='h'),
    'sensor_id': np.random.choice(['A', 'B', 'C'], size=100),
    'value': np.random.normal(loc=0, scale=1, size=100)
}
df = pd.DataFrame(data)


def detect_rolling_zscore_anomalies(df, w=20, z=3.0):
    result = df.copy()

    # Ensure proper temporal order within each sensor before rolling computations.
    result = result.sort_values(['sensor_id', 'timestamp']).copy()

    grouped = result.groupby('sensor_id', group_keys=False)
    prev_values = grouped['value'].shift(1)

    rolling_mean = (
        prev_values
        .groupby(result['sensor_id'])
        .rolling(window=w, min_periods=w)
        .mean()
        .reset_index(level=0, drop=True)
    )

    rolling_std = (
        prev_values
        .groupby(result['sensor_id'])
        .rolling(window=w, min_periods=w)
        .std()
        .reset_index(level=0, drop=True)
    )

    z_score = (result['value'] - rolling_mean) / rolling_std

    # Not enough history (NaN stats) or zero std are marked as non-anomalous.
    valid_stats = rolling_mean.notna() & rolling_std.notna() & (rolling_std > 0)
    result['is_anomaly'] = (z_score.abs() > z) & valid_stats

    # Return in original row order with only the required extra column added.
    result = result.sort_index()
    return result


output_df = detect_rolling_zscore_anomalies(df, w=20, z=3.0)
print(output_df.head())
print('Anomalies detected:', int(output_df['is_anomaly'].sum()))
                               