# Perception of Excessive Sleepiness and Severe Fatigue in Civil Aviation Pilots linked to Irregular Duty Periods

<p style="text-align: center;"> <img src="https://img.shields.io/badge/python 3-pymer4-blue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-pandas-darkblue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-numpy-darkgreen?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-seaborn-green?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-matplotlib-lightblue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/python 3-Jupyter-orange?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> </p>

## What factors influence the perception of extreme conditions of fatigue and sleepiness?

Severe fatigue and excessive sleepiness are critical safety concerns in civil aviation, and their contributing factors are multifactorial and interdependent. This study investigated how personal characteristics, sleep‑related behaviors, and work‑routine conditions shape pilots’ perceptions of severe fatigue and excessive sleepiness during irregular duty periods. Over a six‑month period, 48 pilots repeatedly reported their levels of sleepiness and fatigue at the start, middle, and end of workshifts using the Karolinska Sleepiness Scale and the Samn–Perelli Fatigue Scale. More than 30 features were derived from participant questionnaires and operational data. Two mixed‑effects logistic regression models were used to quantify the influence of time awake, sleep quality, sleep duration, age, duty timing, and workshift progression on fatigue and sleepiness‑related perceptions. Work‑related factors particularly reaching the end of a duty period, operating during the night window (00:00–05:00), and longer duty duration substantially increased the odds of reporting severe fatigue or excessive sleepiness. Personal factors such as being awake for more than 10 hours and being in the mid‑career age range also elevated risk. In contrast, higher perceived sleep quality and sleeping more than five hours before duty were protective. These findings highlight the need for fatigue risk management strategies that integrate both individual sleep behaviors and structural characteristics of duty schedules.

<p float="left">
  <img src="/figures/04.coeffs_odds.png" width="400" />
  <img src="/figures/05.coeffs_odds.png" width="400" /> 
</p>

---
## Quantification

### Perception of Excessive Sleepiness

>- **Early-Morning and Evening periods:**
Participants have **3.0 (1.9, 4.8)** times the odds of perceiving excessive sleepiness compared with the Afternoon period, holding all other covariates constant.
>
>- **Night period:**
Participants have **4.5 (2.5, 8.1)** times the odds of perceiving excessive sleepiness compared with the Afternoon period, holding all other covariates constant.
>
>- **Middle of the workshift:**
Participants have **3.3 (2.9, 3.6)** times the odds of perceiving excessive sleepiness compared with the start of the workshift, holding all other covariates constant.
>
>- **End of the workshift:**
Participants have **13.3 (7.7, 23.3)** times the odds of perceiving excessive sleepiness compared with the start of the workshift, holding all other covariates constant.
>
>- **Workshifts including the Night period (00:00–05:00):**
Participants have **1.8 (1.2, 2.8)** times the odds of perceiving excessive sleepiness compared with workshifts that do not include this period, holding all other covariates constant.
>
>- **Sleep duration > 5 hours before the workshift:**
Participants have **0.49 (0.30, 0.80)** times the odds—equivalently, 51% (20%, 70%) lower odds—of perceiving excessive sleepiness compared with those who slept ≤5 hours, holding all other covariates constant.
>
>- **Higher perceived sleep quality before the workshift:**
Participants have **0.49 (0.38, 0.63)** times the odds—equivalently, 51% (62%, 37%) lower odds—of perceiving excessive sleepiness compared with the reference sleep-quality level, holding all other covariates constant.
>
>- **Awake for more than 10 hours before the workshift:**
Participants have **2.1 (1.1, 4.2)** times the odds of perceiving excessive sleepiness compared with those awake ≤10 hours, holding all other covariates constant.

### Perception of Severe Fatigue

>- **End of the workshift:**
Participants have **25 (12, 53)** times the odds of perceiving severe fatigue compared with the start and middle of the workshift, holding all other covariates constant.
>
>- **Work routines including the Night period (00:00–05:00):**
Participants have **3.4 (1.8, 6.6)** times the odds of perceiving severe fatigue compared with routines that do not include this period, holding all other covariates constant.
>
>- **Every additional 2 hours of work:**
The odds of perceiving severe fatigue increase by a factor of **2.1 (1.5, 2.8)** for each additional 2 hours worked, relative to any baseline, holding all other covariates constant.
>
>- **Higher perceived sleep quality before the workshift:**
Participants have **0.37 (0.25, 0.55)** times the odds—equivalently, 63% (75%, 45%) lower odds—of perceiving severe fatigue compared with the reference sleep-quality level, holding all other covariates constant.
>
>- **Middle-career individuals (ages 35–45):**
Participants in this age range have **3.2 (1.3, 7.9)** times the odds of perceiving severe fatigue compared with younger and older professionals, holding all other covariates constant.
>
>- **Awake for more than 10 hours before the workshift:**
Participants have **9.0 (3.8, 21.0)** times the odds of perceiving severe fatigue compared with those awake ≤10 hours, holding all other covariates constant.

---

## Model Description

The mixed-effects binomial model with logistic link can be described as:

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
