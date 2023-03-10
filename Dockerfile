FROM python:3.8.0-slim as builder


RUN apt-get -y update && apt-get install -y --no-install-recommends \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt .
RUN pip3 install -r requirements.txt 


COPY app ./opt/app

WORKDIR /opt/app


ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/app:${PATH}"

RUN chmod +x train.py \
 && chmod +x test.py \
 && chmod +x serve.py 

RUN chown -R 1000:1000 /opt/app/  && \
    chown -R 1000:1000 /var/log/nginx/  && \
    chown -R 1000:1000 /var/lib/nginx/

USER 1000

CMD ["python", "serve.py"]