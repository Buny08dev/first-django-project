FROM python:3.11-slim

RUN groupadd -r nonroot && useradd -r -s /bin/sh -g nonroot -u 1234 anonimus
# RUN useradd -s /bin/sh -u 1234 anonimus

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat-openbsd

RUN mkdir media

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
# RUN chmod +x /usr/src/app/entrypoint.sh
# RUN chown -R anonimus:nonroot /usr/src/app
RUN mkdir -p media staticfiles && \
    sed -i 's/\r$//g' entrypoint.sh && \
    chmod +x entrypoint.sh && \
    chown -R anonimus:nonroot /usr/src/app

USER anonimus

ENTRYPOINT [ "./entrypoint.sh" ]