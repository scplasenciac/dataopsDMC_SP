FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY data/ComisionEmpleados_V1_202605.csv ./data/

CMD ["python", "script_comisiones.py"]