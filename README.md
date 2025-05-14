# Observabilidade

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Observabilidade

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         obs-metrics and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, examples, and all other explanatory materials.
│
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── obs-metrics   <- Source code for use in this project.
    │
    ├── __init__.py            <- Makes obs-metrics a Python module
    │
    ├── config.py              <- Store useful variables and configuration
    │
    ├── looger.py              <- Structured Logging
    │
    ├── middleware            <- Middlewares for frameworks
    │
    └── logs.sink.py           <- Send to Elasticsearch/Logstash
    
```

--------

