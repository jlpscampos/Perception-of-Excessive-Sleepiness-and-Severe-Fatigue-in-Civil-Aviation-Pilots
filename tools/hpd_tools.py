import numpy as np
from scipy import optimize
from scipy.stats import beta
from scipy.special import betaln, gammaln
from typing import Tuple

def mom_beta_adjusted(y: np.ndarray, n: np.ndarray) -> Tuple[float,float]:
    y = np.asarray(y, dtype=float)
    n = np.asarray(n, dtype=float)
    if y.shape != n.shape:
        raise ValueError("y and n must have same shape")
    K = len(y)
    if K < 1:
        raise ValueError("need at least one group")
    p = np.divide(y, n, where=(n>0))
    pooled_m = y.sum() / n.sum()
    S2 = p.var(ddof=1) if K > 1 else 0.0
    mean_binom_var = np.mean(np.where(n > 0, pooled_m * (1 - pooled_m) / n, 0.0))
    sigma2_between = S2 - mean_binom_var
    if sigma2_between <= 0:
        large_phi = 1e6
        return pooled_m * large_phi, (1.0 - pooled_m) * large_phi
    V_true = sigma2_between
    phi = (pooled_m * (1.0 - pooled_m)) / V_true - 1.0
    if phi <= 0:
        large_phi = 1e6
        return pooled_m * large_phi, (1.0 - pooled_m) * large_phi
    alpha = pooled_m * phi
    beta_ = (1.0 - pooled_m) * phi
    return float(alpha), float(beta_)

def beta_log_marginal(params, y, n):
    log_alpha, log_beta = params
    a = np.exp(log_alpha)
    b = np.exp(log_beta)
    ll = 0.0
    for yi, ni in zip(y, n):
        ll += gammaln(ni + 1) - gammaln(yi + 1) - gammaln(ni - yi + 1)
        ll += betaln(a + yi, b + ni - yi) - betaln(a, b)
    return -float(ll)

def mle_beta_marginal(y: np.ndarray, n: np.ndarray, init_alpha_beta=None) -> Tuple[float,float]:
    y = np.asarray(y, dtype=float)
    n = np.asarray(n, dtype=float)
    if init_alpha_beta is None:
        init_alpha_beta = mom_beta_adjusted(y, n)
    a0, b0 = init_alpha_beta
    x0 = np.log([max(a0, 1e-6), max(b0, 1e-6)])
    res = optimize.minimize(beta_log_marginal, x0, args=(y, n),
                            bounds=[(None, None), (None, None)],
                            method='L-BFGS-B')
    if not res.success:
        return float(a0), float(b0)
    a_hat, b_hat = np.exp(res.x)
    return float(a_hat), float(b_hat)

def sample_hpd(samples: np.ndarray, mass: float = 0.95) -> Tuple[float,float]:
    s = np.sort(np.asarray(samples))
    N = len(s)
    if N == 0:
        raise ValueError("no samples provided")
    k = max(1, int(np.floor(mass * N)))
    widths = s[k-1:] - s[:N-k+1]
    idx = np.argmin(widths)
    return float(s[idx]), float(s[idx + k - 1])

def beta_hpd_by_density(a: float, b: float, mass: float = 0.95, grid_points: int = 20001) -> Tuple[float,float]:
    # density-threshold HPD: find t such that integral of pdf where pdf>=t equals mass
    if not (0.0 < mass < 1.0):
        raise ValueError("mass must be between 0 and 1")
    xs = np.linspace(0, 1, grid_points)
    pdf_vals = beta.pdf(xs, a, b)
    # if pdf is nan at boundaries for extreme a,b, replace with limits
    pdf_vals = np.nan_to_num(pdf_vals, nan=0.0, posinf=0.0, neginf=0.0)
    # sort pdf thresholds
    sorted_idx = np.argsort(pdf_vals)[::-1]  # descending by density
    cum_mass = 0.0
    dx = xs[1] - xs[0]
    included = np.zeros_like(xs, dtype=bool)
    for idx in sorted_idx:
        included[idx] = True
        cum_mass += pdf_vals[idx] * dx
        if cum_mass >= mass:
            break
    included_xs = xs[included]
    return float(included_xs.min()), float(included_xs.max())

def robust_beta_hpd(a: float, b: float, mass: float = 0.95, samples: int = 50000, method: str = "sample") -> Tuple[float,float]:
    """
    Robust HPD wrapper.
    method: "sample" (default) uses posterior sampling + sliding window.
            "density" uses density-threshold grid integration (deterministic).
    """
    if method == "sample":
        draws = np.random.beta(a, b, size=samples)
        return sample_hpd(draws, mass=mass)
    elif method == "density":
        return beta_hpd_by_density(a, b, mass=mass)
    else:
        raise ValueError("method must be 'sample' or 'density'")

def empirical_bayes_posteriors(y: np.ndarray, n: np.ndarray, use_mle: bool = False, mass: float = 0.95, hpd_method: str = "sample"):
    y = np.asarray(y, dtype=float)
    n = np.asarray(n, dtype=float)
    if use_mle:
        alpha0, beta0 = mle_beta_marginal(y, n)
    else:
        alpha0, beta0 = mom_beta_adjusted(y, n)
    K = len(y)
    post_a = np.empty(K)
    post_b = np.empty(K)
    post_mean = np.empty(K)
    hpd_low = np.empty(K)
    hpd_up = np.empty(K)
    for i in range(K):
        a = alpha0 + y[i]
        b = beta0 + n[i] - y[i]
        post_a[i] = a
        post_b[i] = b
        post_mean[i] = a / (a + b)
        # use robust HPD (sample-based by default)
        l, u = robust_beta_hpd(a, b, mass=mass, method=hpd_method)
        hpd_low[i] = l
        hpd_up[i] = u
    return (alpha0, beta0), (post_a, post_b, post_mean, hpd_low, hpd_up)

# Example usage
#if __name__ == "__main__":
#    y = np.array([77, 11, 2])
#    n = np.array([384, 306, 389])
#    (alpha0, beta0), (post_a, post_b, post_mean, hpd_low, hpd_up) = empirical_bayes_posteriors(
#        y, n, use_mle=False, mass=0.95, hpd_method="sample"
#    )
#    print("Estimated prior alpha,beta:", alpha0, beta0)
#    for i in range(len(y)):
#        print(f"group {i}: y={int(y[i])}/{int(n[i])}, posterior mean={post_mean[i]:.4f}, HPD95=[{hpd_low[i]:.4f}, {hpd_up[i]:.4f}]")