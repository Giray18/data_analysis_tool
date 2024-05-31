FROM python:3.11

# set the working directory
# WORKDIR /code
WORKDIR /data

# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the src to the folder
COPY ./src ./src
# COPY src/mysql_works.py ./

# RUN chmod +x

# start the server
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
# CMD [ "--host", "0.0.0.0", "--port", "80", "--reload"]
CMD ["python3", "src/mysql_works.py"]
# , "start", "--config", "config.yml"]
# ,"--host", "0.0.0.0", "--port", "80", "--reload"]