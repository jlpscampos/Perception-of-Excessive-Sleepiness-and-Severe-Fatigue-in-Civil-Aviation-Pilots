# Perception of Excessive Sleepiness and Severe Fatigue in Civil Aviation Pilots linked to Irregular Duty Periods

<p style="text-align: center;"> <img src="https://img.shields.io/badge/python 3-pymer4-blue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-pandas-darkblue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-numpy-darkgreen?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-seaborn-green?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-matplotlib-lightblue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-Jupyter-orange?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> </p>

## What factors influence the perception of extreme conditions of fatigue and sleepiness?

Severe fatigue and excessive sleepiness are critical safety concerns in civil aviation, and their contributing factors are multifactorial and interdependent. This study investigated how personal characteristics, sleep‑related behaviors, and work‑routine conditions shape pilots’ perceptions of severe fatigue and excessive sleepiness during irregular duty periods. Over a six‑month period, 48 pilots repeatedly reported their levels of sleepiness and fatigue at the start, middle, and end of workshifts using the Karolinska Sleepiness Scale and the Samn–Perelli Fatigue Scale. More than 30 features were derived from participant questionnaires and operational data. Two mixed‑effects logistic regression models were used to quantify the influence of time awake, sleep quality, sleep duration, age, duty timing, and workshift progression on fatigue‑ and sleepiness‑related perceptions. Work‑related factors—particularly reaching the end of a duty period, operating during the night window (00:00–05:00), and longer duty duration—substantially increased the odds of reporting severe fatigue or excessive sleepiness. Personal factors such as being awake for more than 10 hours and being in the mid‑career age range also elevated risk. In contrast, higher perceived sleep quality and sleeping more than five hours before duty were protective. These findings highlight the need for fatigue‑risk management strategies that integrate both individual sleep behaviors and structural characteristics of duty schedules.

<p float="left">
  <img src="/figures/04.coefs_odds.png" width="400" />
  <img src="/figures/05.coefs_odds.png" width="400" /> 
</p>

---

## Model Description

The binomial mixed model with logistic link can be described as:

$$ g(x_{ij},\beta_{0i},\beta_{s}) = \beta_{0i}+\boldsymbol{x_{ij}^{\prime}}\\boldsymbol{\beta_s} $$

$$ \beta_{0i} = \beta_0 + \alpha_i $$

$$ \alpha_i \sim N(0,\sigma_{\alpha}^{2}) $$

where $\beta_0$ is the intercept and $\alpha_i$ is the random intercept due to participant clusters.

The logistic link function is given by:

$$  g(x_{ij},\beta_{0i},\beta_{s}) = ln\left[\frac{\pi(x_{ij},\cdot)}{1-\pi(x_{ij},\cdot)}\right] $$

with,

$$ \pi(x_{ij},\cdot) = \frac{e^{\beta_{0i}+\boldsymbol{x_{ij}^{\prime}}\\boldsymbol{\beta_s}}}{1+e^{\beta_{0i}+\boldsymbol{x_{ij}^{\prime}}\\boldsymbol{\beta_s}}} $$

---

## References

This case study is a reformulation of a consultancy provided by the owner of the repository to the Public Health Faculty of the University of São Paulo through the [Centre for Applied Statistics of the University of São Paulo](https://www.ime.usp.br/cea/) and can be accessed at [Repositorio USP](https://repositorio.usp.br/item/003118043)
