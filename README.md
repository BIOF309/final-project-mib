MIB Group Final Project
==============================

The following project presents four graphs of **obesity and mental health** prevalence in the United States.
We have compared gender and age group across the US in an attempt to better understand the link between the two diseases.

##### Figure 1 shows obesity and depression rates over time for adults.
![obesity_and_depression_linegraphs](https://github.com/BIOF309/final-project-mib/blob/master/obesity_and_depression_linegraphs.PNG)

##### Figure 2 shows the prevalence of any mental health disorder in 2016 by gender and various age groups
![bar_graph_mental_health](https://github.com/BIOF309/final-project-mib/blob/master/bar_graph_mental_health.PNG)


#### Figure 3 shows the prevalence of people with both obesity and depression by age group and gender
![depression_and_obesity_graphs](https://github.com/BIOF309/final-project-mib/blob/master/depression_and_obesity_graphs.PNG) 


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├    │
    ├  │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
