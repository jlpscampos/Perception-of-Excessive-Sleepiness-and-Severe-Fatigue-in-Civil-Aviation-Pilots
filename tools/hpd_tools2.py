import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

def fit_multilevel_logistic(df, draws=1000, tune=500, seed=123):
    # index mapping
    participants, participant_idx = np.unique(df['participant_id'], return_inverse=True)
    periods, period_idx = np.unique(df['period_id'], return_inverse=True)
    I = len(participants)
    T = len(periods)

    y = df['y'].values.astype(int)
    n = df['n'].values.astype(int)

    with pm.Model() as model:
        # Priors for period-level log-odds
        mu_period = pm.Normal("mu_period", mu=0.0, sigma=2.5, shape=T)

        # Participant-level random intercepts
        sigma_b = pm.HalfNormal("sigma_b", sigma=1.0)
        b = pm.Normal("b", mu=0.0, sigma=sigma_b, shape=I)

        # Linear predictor and likelihood
        logit_p = mu_period[period_idx] + b[participant_idx]
        p = pm.math.sigmoid(logit_p)
        y_obs = pm.Binomial("y_obs", n=n, p=p, observed=y)

        # Sample
        trace = pm.sample(draws=draws, tune=tune, random_seed=seed,
                          chains=2, cores=1, init="adapt_diag",
                          target_accept=0.95, return_inferencedata=True)

    return model, trace, participants, periods

# -------------------------
# Post-processing helpers
# -------------------------
def summarize_periods(trace, periods, cred_mass=0.95):
    # extract mu_period draws shape (chain, draw, T)
    mu_draws = trace.posterior["mu_period"].stack(sample=("chain", "draw")).values  # shape (T, S) or (S, T) depending on pm version
    # ensure shape (S, T)
    if mu_draws.ndim == 2 and mu_draws.shape[0] == len(periods):
        mu_draws = mu_draws.T
    p_draws = 1 / (1 + np.exp(-mu_draws))  # shape (S, T)
    mean = p_draws.mean(axis=0)
    lower = np.quantile(p_draws, (1-cred_mass)/2, axis=0)
    upper = np.quantile(p_draws, 1-(1-cred_mass)/2, axis=0)
    median = np.quantile(p_draws, 0.5, axis=0)
    df = pd.DataFrame({
        'period': periods,
        'mean': mean,
        'median': median,
        f'lower_{int(100*cred_mass)}': lower,
        f'upper_{int(100*cred_mass)}': upper
    })
    return df, p_draws
    