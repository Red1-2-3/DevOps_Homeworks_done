FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN chmod +x app.py
EXPOSE 8082
CMD ["python", "app.py"]
