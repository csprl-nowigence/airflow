# airflow
Learning Airflow

Doing [basic local installation](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)

```shell
# Install Airflow using the constraints file
AIRFLOW_VERSION=2.2.4
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
```
- Airflow version: 2.2.4
- Python Version: 3.8.8

```shell
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
pip install apache-airflow-providers-mongo
python -m pip airflow standalone
```

I had to upgrade the cryptography package for this to work on my M1 Mac.  
Ended up with version 36.0.1
```shell
pip install -U cryptograhy
```

[Caddy config](./Caddyfile) for fcm.

Tutorials
- [basic dag](https://www.analyticsvidhya.com/blog/2020/11/getting-started-with-apache-airflow/) (old, super basic, kinda lousy, I didn't follow it exactly)
  - [`./tut_av/terminal_output.py`](./tut_av/terminal_output.py)
- [variables / python operator](https://www.analyticsvidhya.com/blog/2020/11/data-engineering-101-getting-started-with-python-operator-in-apache-airflow/)
  - [`./tut_av/python_op.py`](./tut_av/python_op.py)
  - [`./tut_av/variables.py`](./tut_av/variables.py)