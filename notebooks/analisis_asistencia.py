import pandas as pd

#Extraer información 
data_frame_asistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#Extraer datos básicos de la data ingresada

#print(data_frame_asistencia.head(100))
#print(data_frame_asistencia.tail())
#print(data_frame_asistencia.info())
#print(data_frame_asistencia.describe())
print(data_frame_asistencia['estrato'].value_counts().head(2))

#FILTROS Y CONDICIONES PARA TRANSFORMAR DATOS
#1. Reportar todos los estudiantes que asistieron
#2. Reportar todos los estudiantes que faltaron
#3. Reportar todos los estudiantes que llegaron tarde (Justificado)
#4. Reportar todos los estudiantes de estrato 1
#5. Reportar todos los estudiantes de estrato altos
#6. Reportar todos los estudiantes que llegan en metro
#7. Reportar todos los estudiantes que llegan en bicicleta.
#8. Reportar todos los estudiantes que no caminan para llegar a la u
#9. Reportar todos los registros de asistencia del mes de junio
#10. Reportar los estudiantes que faltaron y usan bus para llegar a la Uni
#11. Reportar estudiantes que usan bus y son de estratos altos
#12. Reportar estudiantes que usan bus y son de estratos bajos.
#13. Reportar estudiantes que llegan tarde y sond de estrato 3,4, 5 0 6
#14. Reportar estudiantes que usan transportes ecológicos
#15. Reportar estudiantes que faltan y usan carros para transportarse 
#16. Reportar estudiantes que asisten son estratos altos y caminan
#17. Reportar estudiantes que son estratos bajos y justifican su inasistencia
#18. Reportar estudiantes que son estratos altos y justifican su inasistencia
#19. Reportar estudiantes que usan carro y jsutrifican su inasistencia
#20. Reportar estudiantes que faltan y usan metro y son estratos medios.
 

#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
#2. Número de registro por estrato
#3. Cantidad de estudiantes por medio de transporte
#4. Cantidad de registros por grupo 
#5. Cruce entre estado y medio de transporte 
#6. Promedio de estrato por estado de asistencia
#7. Estrato promedio por medio de transporte
#8. Máximo estrato por estado de asistencia
#9. Mínimo estrato or estado de asistencia
#10. Conteo de asistencias por grupo y por estado
#11. Transporte usado por grupo
#12. Cuantos grupos distintos registraron asistencia por fecha
#13. Promedio de estrato por fecha 
#14. Número de tipos de estado por transporte
#15. Primer registro de cada grupo 