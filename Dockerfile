FROM python:3.8-slim
WORKDIR /home/mooovement

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

CMD ["python","-u", "listen.py"]
