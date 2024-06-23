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
    c.drawString(150, height - 35, "Reporte de número de reservas del cliente")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "por mes en una discoteca")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 90, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este reporte presenta una proyección del número esperado de reservas "
            "para cada día de la semana, basada en el análisis histórico de datos de reservas. Hemos utilizado técnicas "
            "de regresión lineal para modelar la relación entre el día de la semana y el número de reservas, lo que nos "
            "permite realizar predicciones con un cierto grado de confianza.")
    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    p = Paragraph(text, style)
    p.wrapOn(c, width - 150, height - 300)
    p.drawOn(c, 80, height - 170)

    # Agregar el gráfico al pie de la página
    #fig = figs[0]
    figs.savefig("temp_plot.png")  # Guardar el gráfico como imagen temporal
    c.drawImage("temp_plot.png", 100, 300, width=400, height=300)  # Ajustar la posición vertical e horizontal

    # Eliminar la imagen temporal después de usarla
    os.remove("temp_plot.png")

    # Firmas
    c.drawString(100, 230, "Ing. Rodian Raskólnikov")
    c.drawString(130, 215, "Ing. Sistemas.")
    c.drawString(400, 230, "Ing. Oscar Quiroga")
    c.drawString(430, 215, "Director.")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer

def create_pdf2(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height - 35, "Reporte del numero de reservas")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "en una fecha en todas las dicotecas")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 90, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este reporte presenta una proyección del número esperado de reservas "
            "para cada día de la semana, basada en el análisis histórico de datos de reservas. Hemos utilizado técnicas "
            "de regresión lineal para modelar la relación entre el día de la semana y el número de reservas, lo que nos "
            "permite realizar predicciones con un cierto grado de confianza.")
    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    p = Paragraph(text, style)
    p.wrapOn(c, width - 150, height - 300)
    p.drawOn(c, 80, height - 170)

    # Guardar el gráfico en un archivo temporal
    temp_plot_file = "temp_plot.png"
    figs.savefig(temp_plot_file)

    # Ajustar el tamaño y la posición vertical del gráfico en el PDF
    c.drawImage(temp_plot_file, 100, 300, width=400, height=300, preserveAspectRatio=True, anchor="c")

    # Eliminar la imagen temporal después de usarla
    os.remove(temp_plot_file)

    # Firmas
    c.drawString(100, 230, "Ing. Rodian Raskólnikov")
    c.drawString(130, 215, "Ing. Sistemas.")
    c.drawString(400, 230, "Ing. Oscar Quiroga")
    c.drawString(430, 215, "Director.")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer


def create_pdf3(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height - 35, "Reporte de reservas")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "por mes en una discotec")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 90, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este reporte presenta una proyección del número esperado de reservas "
            "para cada día de la semana, basada en el análisis histórico de datos de reservas. Hemos utilizado técnicas "
            "de regresión lineal para modelar la relación entre el día de la semana y el número de reservas, lo que nos "
            "permite realizar predicciones con un cierto grado de confianza.")
    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    p = Paragraph(text, style)
    p.wrapOn(c, width - 150, height - 300)
    p.drawOn(c, 80, height - 170)

    # Agregar el gráfico al pie de la página
    #fig = figs[0]
    figs.savefig("temp_plot.png")  # Guardar el gráfico como imagen temporal
    c.drawImage("temp_plot.png", 100, 300, width=400, height=300)  # Ajustar la posición vertical e horizontal

    # Eliminar la imagen temporal después de usarla
    os.remove("temp_plot.png")

    # Firmas
    c.drawString(100, 230, "Ing. Rodian Raskólnikov")
    c.drawString(130, 215, "Ing. Sistemas.")
    c.drawString(400, 230, "Ing. Oscar Quiroga")
    c.drawString(430, 215, "Director.")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer