# Perception of Excessive Sleepiness and Severe Fatigue in Civil Aviation Pilots linked to Irregular Duty Periods

<p style="text-align: center;"> <img src="https://img.shields.io/badge/Python 3-pymer-blue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-pandas-darkblue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-numpy-darkgreen?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-seaborn-green?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-matplotlib-lightblue?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> <img src="https://img.shields.io/badge/Python 3-Jupyter-orange?logo=SimpleIconName&logoColor=ColorName&style=ShieldStyle" /> </p>

This study assess the relationship between irregular duty periods and the perceptions of excessive sleepiness and severe fatigue through the self reported perception of sleepiness, using the [Karolinska Sleepiness Scale](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5511283/), and fatigue, using the [Sam-Perelli Fatigue Scale](https://psycnet.apa.org/record/2017-30931-005) at the beginning, middle and end of duty period or workload. The study was carried out longitudinally over two semesters and was evaluated using a cluster-specific binomial model with logistic link.


This repository includes:

* Data: Raw data collected from pilot surveys, actimetry, and other sources (upon request).
* Code: Scripts for data cleaning, analysis, and visualization using relevant Python libraries.
* Analysis: Reports and documentation detailing the methodology, results, and conclusions.
* Jupyter Notebooks: Interactive python Markdown documents for exploring the data and results.

The Jupyter Notebooks follows the order:

* Data preparation, feature extratction and data cleaning [feature_engineering.ipynb](feature_engineering.ipynb)
* Exploratory Data Analysis [EDA.ipynb](Exploratory_Data_Analysis.ipynb)
* Results related to perception of sleepiness [regression_sleepiness.ipynb](regression_sleepiness_2.ipynb)
* Results related to perception of fatigue [regression_fatigue.ipynb](regression_fatigue.ipynb)

This project aims to contribute to the understanding of work and personal related factors leading to perception of excessive/severe sleepiness/fatigue in civil aviation pilots.

---

## Brief Abstract

Over recent decades, growing concerns about labour-life quality and health have ignited extensive discussions within industry and legislative bodies. In the specific domain of civil aviation, workers life quality emerges as a pivotal factor intricately linked to the regularity and duration of pilot duty periods. In Brazil, the “Lei do Aeronauta” (Law of the Airman), enacted in 1984, established regulations governing the maximum duration of workloads and mandated a minimum number of monthly days off for pilots. Recognizing the imperative to enhance the quality of life for commanders and co-pilots, this law underwent revision in 2017, notably increasing monthly days off, reducing permitted workload durations, and limiting consecutive workloads, including early-start (duties starting between 05:00 - 07:59) and night (between 00:00 - 04:59) routines. This study aims to quantify the impact of irregular workloads on pilot quality of life, focusing on perceived fatigue and sleepiness. Conducted longitudinally on 48 participants between the summer and autumn of 2022, pilots self-reported their perceived sleepiness and fatigue using the Karolinska and Sam-Perelli scales, respectively. Time varying metrics obtained from punch clock, actimetry and sleep diaries and time invariant metrics such as sociodemographic data and chronotype were taken. Employing cluster-specific binomial models with logistic link, we found that duties comprehending periods outside the circadian time (Early-Start and Night periods), longer workloads, many hours awake before the start of duty and sleep deprivation are the main enhancement factors for percecption of excessive/severe sleepiness and fatigue, marriage and pilots that have better work performance at morning (chronotypes matutines) are protection factors. Tailored interventions and potential regulatory adjustments are crucial for pilots’ well-being in order to avoid labour risks associated to sleepiness and fatigue.

---

## Main Results

<p float="left">
  <img src="/figures/sleepiness_coeffs_odds.png" width="250" />
  <img src="/figures/fatigue_coeffs_odds.png" width="250" /> 
</p>

---

## Model Description

---

## References

This case study is a reformulation of a consultancy provided by the owner of the repository to the Public Health Faculty of the University of São Paulo through the [Centre for Applied Statistics of the University of São Paulo](https://www.ime.usp.br/cea/) and can be accessed at [Repositorio USP](https://repositorio.usp.br/item/003118043)
