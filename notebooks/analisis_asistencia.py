import pandas as pd

#Extraer información 
data_frame_asistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#Extraer datos básicos de la data ingresada

#print(data_frame_asistencia.head(100))
#print(data_frame_asistencia.tail())
#print(data_frame_asistencia.info())
#print(data_frame_asistencia.describe())
print(data_frame_asistencia['estrato'].value_counts().head(2))
