FROM python:3.8 AS BUILD

COPY ./requirements.txt .

RUN apt-get update && apt-get upgrade -y && \
apt-get install -y libmariadb-dev gcc && \
pip install --no-cache-dir --user -r ./requirements.txt

FROM python:3.8-slim

WORKDIR /app

COPY --from=BUILD /root/.local/lib /root/.local/lib
COPY --from=BUILD /usr/lib/x86_64-linux-gnu/libmariadb.so.3 /usr/lib/x86_64-linux-gnu/libmariadb.so.3

COPY . .

ENV PATH=/root/.local/bin:$PATH

CMD ["python", "./src/main.py"]
