FROM python:3.8 AS BUILD

COPY ./requirements.txt .

RUN pip install --no-cache-dir --user -r ./requirements.txt

FROM python:3.8-slim

WORKDIR /app

COPY --from=BUILD /root/.local/lib /root/.local/lib

COPY . .

ENV DISCORD_TOKEN=ODA4NzI2NDk1MzI1NDU0Mzc2.YCKvPQ.gSqiguOb_SdKiWEccXXqNvbCAJg
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "./src/main.py"]
