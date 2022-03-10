# airflow
Learning Airflow

Following [basic local installation](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html) instructions.

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
# launch airflow
python -m pip airflow standalone
```

I had to upgrade the cryptography package for this to work on my M1 Mac.  
Ended up with version 36.0.1
```shell
pip install -U cryptograhy
```

Adding MongoDB Atlas connection in admin UI:
- host: \<server domain name>
- schema: `admin`  (whatever the path in your connection uri is)
- login: \<user name>
- password: \<password>
- port: **LEAVE THIS EMPTY**  (leave blank for atlas clusters)
- extra: `{"srv": true}`  (for atlas clusters, sets URI scheme to `mongo+srv:`)

[Caddy config](./Caddyfile) for fcm.

This is running on fcm:
- this repo folder: `/root/airflow_exploration/`
- airflow folder: `/root/airflow/`
- pyenv virtualenv: `airflow`
- tmux session: `airflow`

Tutorials
- [basic dag](https://www.analyticsvidhya.com/blog/2020/11/getting-started-with-apache-airflow/) (old, super basic, kinda lousy, I didn't follow it exactly)
  - [`./tut_av/terminal_output.py`](./tut_av/terminal_output.py)
- [variables / python operator](https://www.analyticsvidhya.com/blog/2020/11/data-engineering-101-getting-started-with-python-operator-in-apache-airflow/)
  - [`./tut_av/python_op.py`](./tut_av/python_op.py)
  - [`./tut_av/variables.py`](./tut_av/variables.py)
- [basic pipeline](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)
  - [`./tut_airflow/basic_pipeline.py`](./tut_airflow/basic_pipeline.py)
  - [`./tut_airflow/fetch_to_db.py`](./tut_airflow/fetch_to_db.py)