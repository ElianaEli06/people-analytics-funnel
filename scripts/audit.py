import pandas as pd

# 1. Cargar del "Legajo de Candidatos"
try:
    df_candidates = pd.read_csv('data/candidates.csv')
    print("✅ ¡Archivo de candidatos cargado con éxito!")
    
    # 2. Auditoría rápida (Hito 1)
    print("\n--- Resumen del Dataset ---")
    print(f"Total de candidatos registrados: {len(df_candidates)}")
    
    print("\n--- Verificación de Datos Faltantes ---")
    print(df_candidates.isnull().sum())
    
    print("\n--- Primeras 5 filas del reporte ---")
    print(df_candidates.head())

except FileNotFoundError:
    print("❌ Error: No encuentro el archivo 'candidates.csv'. Asegúrate de que esté en la misma carpeta.")