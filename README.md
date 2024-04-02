# Perception of Fatigue and Sleepiness linked to Irregular Workloads in Civil Aviation

<p style="text-align: center;"> <img src="https://img.shields.io/badge/Python 3-statsmodels-blue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-pandas-darkblue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-numpy-darkgreen?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-seaborn-green?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-matplotlib-lightblue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-Jupyter-orange?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> </p>

This project analyzes data from 48 pilots under the revised "Lei do Aeronauta" (Law of the Airman) to assess the relationship between workload characteristics, pilot characteristics, and perceived fatigue & sleepiness. The project utilizes mixed binomial models and focuses on data collected using the Karolinska Sleepiness Scale and the Sam-Perelli Fatigue Scale.

This repository includes:

* Data: Raw data collected from pilot surveys, actimetry, and other sources (upon request).
* Code: Scripts for data cleaning, analysis, and visualization using relevant Python libraries.
* Analysis: Reports and documentation detailing the methodology, results, and conclusions.
* Jupyter Notebooks: Interactive python Markdown documents for exploring the data and results.

The Jupyter Notebooks follows the order:

* Data preparation, feature extratction and data cleaning [feature_engineering.ipynb](feature_engineering.ipynb)
* Exploratory Data Analysis [EDA.ipynb](EDA.ipynb)
* Results related to perception of sleepiness [regression_sleepiness.ipynb](regression_sleepiness.ipynb)
* Results related to perception of fatigue [regression_fatigue.ipynb](regression_fatigue.ipynb)

This project aims to contribute to the understanding of pilot fatigue and inform interventions and regulations to improve pilot well-being in civil aviation.

---

## Brief Abstract

Over recent decades, growing concerns about labour-life quality and health have ignited extensive discussions within industry and legislative bodies. In the specific domain of civil aviation, workers life quality emerges as a pivotal factor intricately linked to the regularity and duration of pilot workloads. In Brazil, the “Lei do Aeronauta” (Law of the Airman), enacted in 1984, established regulations governing the maximum duration of workloads and mandated a minimum number of monthly days off for pilots. Recognizing the imperative to enhance the quality of life for commanders and co-pilots, this law underwent revision in 2017, notably increasing monthly days off, reducing permitted workload durations, and limiting consecutive workloads, including early-start and night routines. This study aims to quantify the impact of irregular workloads on pilot quality of life, focusing on perceived fatigue and sleepiness. Conducted longitudinally on 48 participants between the summer and autumn of 2022, pilots reported their perceived sleepiness and fatigue using the Karolinska and Sam-Perelli scales, respectively. Time varying metrics obtained from punch clock, actimetry and sleep diaries and time invariant metrics such as sociodemographic data and chronotype were taken as well. Employing mixed binomial models, the study found that perception of excessive (severe) sleepiness (fatigue) are more critical at the end of workloads and at night work-shifts compared to other periods. Factors such as individual chronotype, short sleep duration, long time awake before the workload, workloads comprising night periods (night modality), long travel times from home to work and long workload duration, enhanced the perception of excessive (severe) sleepiness (fatigue). Age, work experience, marriage and higher education are found to be protection factors. Tailored interventions and potential regulatory adjustments are crucial for pilots’ well-being in order to avoid labour risks associated to sleepiness and fatigue.

---

## Main Results

![Figure](figures/fig_resultado.png)

### For time-variant covariates

* The odds of perception of excessive (severe) sleepiness (fatigue) at the **middle of workloads** are 2.41 (2.07) times higher than at the **start of workloads**, with all other covariates held constant;
* The odds of perception of excessive (severe) sleepiness (fatigue) at the **end of workloads** are 8.18 (5.22) times higher than at the **start of workloads**, with all other covariates held constant;

<br/>

* The odds of perception of excessive (severe) sleepiness (fatigue) in **early-mornings** are 2.12 (1.50) times higher than in **afternoons (afternons and mornings)**, with all other covariates held constant;
* The odds of perception of excessive sleepiness in **mornings** are 1.36 times higher than in **afternoons**, with all other covariates held constant;
* The odds of perception of excessive (severe) sleepiness (fatigue) in **evenings** are 1.58 (1.38) times higher than in **afternoons (afternoons and mornings)**, with all other covariates held constant;
* The odds of perception of excessive (severe) sleepiness (fatigue) in **nights** are 4.23 (2.60) times higher than in **afternoons (afternoons and mornings)**, with all other covariates held constant.

<br/>

* For **workload duration**, there is an 6% [OR=1.06] (9% [OR=1.09]) increase in the odds of perception excessive (severe) sleepiness (fatigue) in individuals that works 1 hour more compared to any workload duration baseline, with all other covariates held constant;
* For **time awake before the workload**, there is an 7% [OR=1.07] (4% [OR=1.04]) increase in the odds of perception excessive (severe) sleepiness (fatigue) in individuals that were 1 hour awake before workload compared to any time awake before workload baseline, with all other covariates held constant;
* For **travel time home to work**, there is an 26% [OR=1.26] (16% [OR=1.16]) increase in the odds of perception excessive (severe) sleepiness (fatigue) in individuals that take 1 hour more to travel from home to work compared to any travel time home to work baseline, with all other covariates held constant;
* For **flight hours**, there is an 9% [OR=1.09] (8% [OR=1.08]) increase in the odds of perception excessive (severe) sleepiness (fatigue) in individuals with 1,000 more flight hours compared to any flight hours baseline, with all other covariates held constant;
* For **sleep duration before the workload**, there is an 22% [OR=1.22] (13% [OR=1.13]) increase in the odds of perceiving excessive (severe) sleepiness (fatigue) in individuals who slept 1 hour less compared to any sleep duration baseline, with all other covariates held constant.

<br/>

* The odds of perception of excessive (severe) sleepiness (fatigue) for **workloads comprehending night periods** are 1.52 (1.34) times higher than **other workload modalities**, with all other covariates held constant;

### For time-invariant covariates

* The odds of perception of excessive (severe) sleepiness (fatigue) for **co-pilots** are 2.97 (1.59) times higher than for **commanders**, with all other covariates held constant;
* The odds of perception of excessive sleepiness for **singles** are 2.03 times higher than for **married** participants, with all other covariates held constant;
* The odds of perception of excessive (severe) sleepiness (fatigue) for **individuals without higher education** are 2.04 (1.62) times higher than for individuals **with higher education**, with all other covariates held constant;
* The odds of perception of excessive sleepiness for **chronotypes vespertines** are 2.90 (2.58) higher than for **chronotypes matutines or intermediaries**, with all other covariates held constant;

 <br/>

* For **age**, there is an 41% [OR=1.41] increase in the odds of perceiving severe fatigue in individuals 10 years younger compared to any age baseline, with all other covariates held constant.

---

## Model Description

The participants completed the KSS and SPS scales in response to their irregular work schedules, resulting in an imbalance in KSS and SPS measurements among the participants. Since the measurements were taken longitudinally at repeated times, there are two approaches to address this issue: utilizing a cluster-specific model or a population-averaged model. Given the assumption that each participant possesses unique characteristics and experiences or perceives sleepiness and fatigue differently, we opted for a cluster-specific model. This approach, with its advantages, enables us to estimate both cluster-specific effects and effects akin to population averages.

Bellow follows the applied model:

$$\ g(x_{ijk},\beta_{0ij},\beta_{1},\beta_s) = \beta_{0ij}+\beta_{1j}x_{1}+x_{ijk}^{T}\beta_s$$

$$\ \beta_{0ij} = \beta_0 + \alpha_i + \tau_j$$

$$\ \beta_{1j} = \beta_1 + \gamma_j$$

The first equation represents the level 1 of the chosen model. Both, the second and third equations represent the level 2 of the model representing the random intercept term and the random slope term resepctively. $\alpha_{i} \sim N(0,\sigma_{\alpha}^2)$ represents the random intercept due to participant cluster, $\tau_{j} \sim N(0,\sigma_{\tau}^2)$ represents the random intercept due to work-shifts or time the participant filled KSS and SPS scales and $\gamma_{j} \sim N(0,\sigma_{\gamma}^2)$, represents the random slope due to work-shifts, with $\tau_{j} \perp \gamma_{j}$. 

---

## References

This case study is a reformulation of a consultancy provided by the owner of the repository to the Public Health Faculty of the University of São Paulo through the [Centre for Applied Statistics of the University of São Paulo](https://www.ime.usp.br/cea/) and can be accessed at [Repositorio USP](https://repositorio.usp.br/item/003118043)
