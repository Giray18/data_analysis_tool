FROM python:3.11

# set the working directory
# WORKDIR /code
# WORKDIR /data
WORKDIR /src

# ADD dat /app
# ADD requirements.txt /app



# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# RUN pip install -r requirements.txt
# RUN pip install -e ../dat/
# RUN pip install sys

# copy the src to the folder
# COPY ./src ./dat
COPY ./src ./src
# COPY src/mysql_works.py ./

# RUN chmod +x
EXPOSE 3000

# start the server
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]s
# CMD [ "--host", "0.0.0.0", "--port", "80", "--reload"]
CMD ["python3", "src/mysql_analyzer/mysql_pandas.py"]
# , "start", "--config", "config.yml"]
# ,"--host", "0.0.0.0", "--port", "80", "--reload"]