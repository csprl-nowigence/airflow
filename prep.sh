git fetch
git pull
rm -f ../airflow/dags/*.py
rm -f ../airflow/dags/__pycache__/*.pyc
cp tut*/*.py ../airflow/dags/

rm -rf ../airflow/dags/test_*
cp -r test_* ../airflow/dags
