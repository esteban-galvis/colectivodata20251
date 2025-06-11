import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#GRAFICANDO

#Grafica de Barras
colors=["#0918f9","#e600b8","#ff0075","#ff6c43","#ffbb38","#00ca97"] 

plt.figure(figsize=(8,5))
sns.countplot(x='estado',data=dataFrameAsistencia,palette=colors)
plt.title("Cantidad de registros por estado de asistencia")
plt.xlabel("Estado de asistencia")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()

#Grafica de Torta
#Mostrar proporciones entre dos columnas del DF (proporcion de estudiantes x medio de transporte)

conteoMedioTransporte=dataFrameAsistencia["medio_transporte"].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    conteoMedioTransporte,
    labels=conteoMedioTransporte.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("Blues")
)
plt.title("Distribucion de estudiantes por medio de transporte")
plt.tight_layout()
plt.show()

#Grafico de barras agrupadas
#Se aplica cuando hice cruces en el dataFrame

conteoEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)

conteoEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,6),
    color=colors,
)
plt.title("Registro por estado de asistencia y medio de transporte")
plt.xlabel("Estado de asistencia")
plt.ylabel("Cantidad de registros")
plt.legend(title="Medio de transporte")
plt.tight_layout()
plt.show()

#GRAFICAS PARA EL PROYECTO INTEGRADOR


# Conteo de registros por estado y fecha
dataFrameAsistencia['fecha'] = pd.to_datetime(dataFrameAsistencia['fecha'])

conteo_por_fecha = dataFrameAsistencia.groupby(['fecha', 'estado']).size().reset_index(name='cantidad')

plt.figure(figsize=(12, 6))
sns.lineplot(data=conteo_por_fecha, x='fecha', y='cantidad', hue='estado', palette=colors)
plt.title("Asistencia diaria por estado")
plt.xlabel("Fecha")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()

#Distribución de estudiantes por estrato
conteoEstrato = dataFrameAsistencia["estrato"].value_counts().sort_index()

plt.figure(figsize=(7, 5))
sns.barplot(x=conteoEstrato.index.astype(str), y=conteoEstrato.values, palette="pastel")
plt.title("Distribución de registros por estrato")
plt.xlabel("Estrato socioeconómico")
plt.ylabel("Cantidad de registros")
plt.tight_layout()
plt.show()

#Matriz de asistencia cruzando grupo y estado
grupo_estado = dataFrameAsistencia.groupby(['id_grupo', 'estado']).size().unstack(fill_value=0)

plt.figure(figsize=(10, 6))
sns.heatmap(grupo_estado, annot=True, fmt='d', cmap='YlGnBu')
plt.title("Cantidad de registros por grupo y estado de asistencia")
plt.xlabel("Estado de asistencia")
plt.ylabel("ID del grupo")
plt.tight_layout()
plt.show()

