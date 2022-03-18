git fetch
git pull
rm ../airflow/dags/*.py
rm ../airflow/dags/__pycache__/*.pyc
cp tut*/*.py ../airflow/dags/
