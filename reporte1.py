# pdf_generator.py

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def create_pdf(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(130, height - 30, "Reporte de número de reservas esperadas")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(200, height - 45, "por día de la semana")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 60, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este reporte presenta una proyección del número esperado de reservas "
            "para cada día de la semana, basada en el análisis histórico de datos de reservas. Hemos utilizado técnicas "
            "de regresión lineal para modelar la relación entre el día de la semana y el número de reservas, lo que nos "
            "permite realizar predicciones con un cierto grado de confianza.")
    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    p = Paragraph(text, style)
    p.wrapOn(c, width - 60, height - 400)
    p.drawOn(c, 30, height - 200)

    # Agregar el gráfico al pie de la página
    fig = figs[0]
    fig.savefig("temp_plot.png")  # Guardar el gráfico como imagen temporal
    c.drawImage("temp_plot.png", 100, 100, width=400, height=300)  # Ajustar la posición vertical e horizontal

    # Eliminar la imagen temporal después de usarla
    os.remove("temp_plot.png")

    # Firmas
    c.drawString(100, 50, "Ing. Rodian Raskólnikov")
    c.drawString(100, 35, "Ing. Sistemas.")
    c.drawString(400, 50, "Ing. Oscar Quiroga")
    c.drawString(400, 35, "Director.")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
