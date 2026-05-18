FROM python:3.10-slim

WORKDIR /app
RUN mkdir -p /app/output

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY script_comisiones.py .
COPY data/ComisionEmpleados_V1_202605.csv ./data/

CMD ["python", "script_comisiones.py"]