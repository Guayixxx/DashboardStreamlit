import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('/home/juan-pablo/Documentos/Toma de Decisiones 1/Parcial/GymCleanData.csv')

# Sección 1: Resumen general
st.title("Gym Member Analysis")
st.header("Resumen General")
st.metric("Total Users", len(df))
st.metric("Promedio de Calorías Quemadas", round(df['Calories_Burned'].mean(), 2))

# Proporción de tipos de entrenamiento
st.subheader("Proporción de Tipos de Entrenamiento")
workout_type_counts = df['Workout_Type'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(workout_type_counts, labels=workout_type_counts.index, autopct='%1.1f%%', startangle=140)
ax1.set_title("Proporción de Tipos de Entrenamiento")
st.pyplot(fig1)

# Sección 2: Análisis por género
st.header("Análisis por Género")
gender = st.selectbox("Seleccione Género", df['Gender'].unique())

avg_calories_by_workout_gender = df[df['Gender'] == gender].groupby('Workout_Type')['Calories_Burned'].mean()
fig2, ax2 = plt.subplots()
ax2.bar(avg_calories_by_workout_gender.index, avg_calories_by_workout_gender.values, color='skyblue')
ax2.set_title(f"Calorías Quemadas por Tipo de Entrenamiento ({gender})")
ax2.set_xlabel("Workout Type")
ax2.set_ylabel("Calories Burned")
st.pyplot(fig2)

# Sección 3: Relación entre variables
st.header("Relaciones entre Variables")
scatter_gender = st.selectbox("Género para Análisis de Calorías vs Duración", df['Gender'].unique())
subset = df[df['Gender'] == scatter_gender]
fig3, ax3 = plt.subplots()
for workout_type in subset['Workout_Type'].unique():
    subset_workout = subset[subset['Workout_Type'] == workout_type]
    ax3.scatter(subset_workout['Session_Duration_hours'], subset_workout['Calories_Burned'], label=workout_type, alpha=0.7)

ax3.set_xlabel("Session Duration (hours)")
ax3.set_ylabel("Calories Burned")
ax3.set_title(f"Relación entre Calorías y Duración ({scatter_gender})")
ax3.legend(title="Workout Type")
st.pyplot(fig3)

# Sección 4: Promedio de BPM por nivel de experiencia y tipo de entrenamiento
st.header("Promedio de BPM por Nivel de Experiencia y Tipo de Entrenamiento")
selected_gender = st.selectbox("Seleccione Género para Análisis de BPM", df['Gender'].unique(), key="bpm_gender_selector")

avg_bpm_by_experience_gender = df[df['Gender'] == selected_gender].groupby(['Experience_Level_Cat', 'Workout_Type'])['Avg_BPM'].mean().unstack()

fig4, ax4 = plt.subplots(figsize=(10, 6))
for workout_type in avg_bpm_by_experience_gender.columns:
    ax4.plot(avg_bpm_by_experience_gender.index, 
             avg_bpm_by_experience_gender[workout_type], 
             marker='o', 
             linestyle='-', 
             label=workout_type)

ax4.set_xlabel('Experience Level')
ax4.set_ylabel('Average BPM')
ax4.set_title(f"Average BPM by Experience Level and Workout Type ({selected_gender})")
ax4.grid(True)
ax4.legend(title='Workout Type')
st.pyplot(fig4)

# Sección 5: Relación entre porcentaje de grasa y tipo de entrenamiento
st.header("Porcentaje de Grasa Corporal vs Tipo de Entrenamiento")

# Selector de género para esta gráfica
fat_gender = st.selectbox("Seleccione Género para Análisis de Porcentaje de Grasa", df['Gender'].unique(), key="fat_gender_selector")

# Calcular el promedio de porcentaje de grasa por tipo de entrenamiento para el género seleccionado
avg_fat_by_workout_gender = df[df['Gender'] == fat_gender].groupby('Workout_Type')['Fat_Percentage'].mean()

# Crear el gráfico de barras
fig5, ax5 = plt.subplots(figsize=(8, 6))
ax5.bar(avg_fat_by_workout_gender.index, avg_fat_by_workout_gender.values, color='orange')
ax5.set_xlabel("Workout Type")
ax5.set_ylabel("Average Fat Percentage")
ax5.set_title(f"Average Fat Percentage by Workout Type ({fat_gender})")
ax5.grid(axis='y')

# Mostrar el gráfico en Streamlit
st.pyplot(fig5)
