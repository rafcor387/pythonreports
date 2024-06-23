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
    text = ("Este informe presenta un análisis detallado del número de reservas mensuales realizadas por el cliente" 
            "seleccionado en la discoteca seleccionada. A través de gráficos de barras, se visualiza la distribución de" 
            "reservas a lo largo del año, permitiendo identificar patrones y tendencias en la actividad de reservas." 
            "Además, se proporciona un resumen tabular de los datos filtrados para un análisis más detallado." )
    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    p = Paragraph(text, style)
    p.wrapOn(c, width - 150, height - 320)
    p.drawOn(c, 80, height - 180)

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


def create_pdf4(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height - 35, "Reporte de numero de reservas del cliente")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "por mes y discoteca")

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

def create_pdf5(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height - 35, "Reporte de análisis de Distribución de Reservas")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "por Discoteca en un Mes Seleccionado")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 90, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este reporte presenta un análisis detallado de la distribución de reservas realizadas en diversas discotecas" 
            "durante un mes seleccionado. Utilizando gráficos de violín, se examina la variabilidad en el número de reservas" 
            "(identificadas por su idMesa) entre las diferentes discotecas. Este análisis proporciona una visión clara de cómo"
            "se distribuyen las reservas a lo largo del mes en cada discoteca, lo que puede ser útil para comprender los patrones de"
            "demanda y la popularidad relativa de cada establecimiento durante ese período.")
    styles = getSampleStyleSheet()
    style = styles["BodyText"]
    p = Paragraph(text, style)
    p.wrapOn(c, width - 150, height - 300)
    p.drawOn(c, 80, height - 180)

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

def create_pdf6(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height - 35, "Reporte de nálisis de Reservas ")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "Mensuales por Discoteca")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 90, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este informe presenta un análisis detallado de las reservas realizadas en discotecas durante el mes seleccionado." 
            "Se utiliza un boxplot para visualizar la distribución de las reservas diarias por discoteca, lo que proporciona una" 
            "visión general de cómo varía el número de reservas a lo largo del mes. Este análisis ayuda a identificar patrones y" 
            "tendencias en el comportamiento de reserva, lo que puede ser útil para la gestión y planificación de las operaciones" 
            "de las discotecas.")
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


def create_pdf7(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height - 35, "Reporte de análisis de Reservas ")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "Canceladas por Día")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 90, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este reporte presenta un análisis detallado del número de reservas canceladas por día" 
            "durante el mes seleccionado en la discoteca especificada. Al filtrar los registros según" 
            "el mes y el nombre de la discoteca, se revelan tendencias significativas que pueden ayudar a" 
            "identificar patrones de cancelación y áreas de mejora en la gestión de reservas." 
            "El gráfico de barras proporciona una visualización clara del comportamiento de las cancelaciones"
            "a lo largo del mes, ofreciendo información valiosa para la toma de decisiones y la optimización"
            "de procesos en la gestión de reservas.")
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


def create_pdf8(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height - 35, "Reporte de Reservas Mensuales ")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "por Discoteca")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 90, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este reporte ofrece un análisis detallado de las reservas mensuales realizadas en las discotecas." 
            "Permite a los usuarios seleccionar un mes específico y una discoteca para visualizar el número de "
            "reservas realizadas en cada día del mes. Utilizando esta información, los gestores de las discotecas" 
            "pueden obtener una comprensión clara de los patrones de reservas mensuales y tomar decisiones informadas" 
            "para optimizar la gestión de sus establecimientos.")
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



def create_pdf9(figs, logo_path="logo6.jpg"):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo
    logo = ImageReader(logo_path)
    c.drawImage(logo, 30, height - 80, width=80, height=80)

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(150, height - 35, "Reporte de análisis de Reservas ")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 60, "Mensuales por Discoteca")

    # Fecha
    c.setFont("Helvetica", 12)
    date_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    c.drawString(400, height - 90, f"Fecha: {date_str}")

    # Párrafo
    text = ("Este reporte presenta un análisis detallado de las reservas mensuales por discoteca." 
            "Utilizando datos recopilados durante el mes seleccionado, se han examinado las tendencias" 
            "de reserva en cada establecimiento. El informe ofrece una visión general de la distribución" 
            "de las reservas a lo largo del mes, destacando los días de mayor actividad y las preferencias" 
            "de los clientes en términos de discotecas. ")
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