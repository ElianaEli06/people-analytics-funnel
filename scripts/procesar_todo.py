import pandas as pd
import os

# 1. Definimos las rutas (Para que Python no se pierda)
# Buscamos los archivos dentro de la carpeta 'data'
path_data = 'data/'

print("--- 🛠️ Iniciando el Re-armado del Proyecto (Modo Experta) ---")

try:
    # 2. Cargamos la info
    candidatos = pd.read_csv(f'{path_data}candidates.csv')
    pipeline = pd.read_csv(f'{path_data}pipeline.csv')
    performance = pd.read_csv(f'{path_data}performance_fact.csv')
    onboarding = pd.read_csv(f'{path_data}onboarding.csv')
    
    print("✅ Archivos encontrados y cargados con éxito.")

    # 3. Unimos todo (El famoso Merge)
    # Candidatos + Onboarding
    df = pd.merge(candidatos, onboarding, left_on='id', right_on='candidate_id', how='left')
    
    # + Performance
    df_final = pd.merge(df, performance, on='candidate_id', how='left', suffixes=('', '_perf'))

    # 4. Limpiamos un poco
    df_final['rating_6m'] = df_final['rating_6m'].fillna(0)

    # 5. Guardamos el Master Dataset en la carpeta principal
    df_final.to_csv('master_hr_data.csv', index=False)
    
    print("\n✨ ¡LOGRADO! El Master Dataset se actualizó correctamente.")
    print("📍 Ubicación: Carpeta principal / master_hr_data.csv")

except Exception as e:
    print(f"\n❌ Algo salió mal: {e}")
    print("💡 Tip: Asegurate de que la terminal diga que estás en la carpeta principal del proyecto.")