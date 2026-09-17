# 🎮 SoloQ Pulse — Análisis Competitivo

<p align="center">
  <strong>Proyecto integral de Data Analytics para portfolio</strong><br>
  Python · SQL · Power BI · Calidad de Datos · Analítica de Producto
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Analytics-informational?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/SQL-Analysis-informational?logo=postgresql" alt="SQL">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-informational?logo=powerbi" alt="Power BI">
  <img src="https://img.shields.io/badge/Data-Quality-informational" alt="Calidad de Datos">
</p>

---

## 📌 Descripción del proyecto

**SoloQ Pulse** es un caso de estudio ficticio de Data Analytics diseñado para simular el tipo de trabajo que podría realizar un Data Analyst, BI Analyst o Product Analyst dentro de una plataforma de gaming competitivo.

El objetivo no es simplemente crear gráficos, sino desarrollar un flujo completo de análisis:

**Pregunta de negocio → validación de datos → transformación → análisis con SQL/Python → KPI → Dashboard → Insight de negocio → Acción → Medición**

> ⚠️ **Aviso sobre los datos:** todas las observaciones son sintéticas y fueron generadas específicamente para este proyecto de portfolio. No corresponden a datos de Riot Games, OP.GG ni a jugadores reales.

---

## 🎯 Problema de negocio

Un equipo de producto ficticio quiere comprender:

- ¿Qué comportamientos de los jugadores están asociados con la victoria?
- ¿Cómo se relacionan el rol, campeón y estilo de juego con el rendimiento?
- ¿Qué jugadores muestran un rendimiento consistente a lo largo del tiempo?
- ¿Qué importancia tienen los objetivos en comparación con las estadísticas de combate?
- ¿Qué métricas podrían utilizarse para mejorar el feedback posterior a las partidas y el engagement de los jugadores?

El análisis busca responder estas preguntas utilizando evidencia y datos, en lugar de basarse únicamente en visualizaciones aisladas.

---

## 📊 Datos disponibles

| Dataset | Registros | Descripción |
|---|---:|---|
| `matches` | 1.800 | Contexto de las partidas, duración, parche, equilibrio de MMR y resultado |
| `match_participants` | 18.000 | Métricas individuales de combate, CS, visión, oro y objetivos |
| `players` | 80 | Cuenta, tier, rol, región y atributos de estilo de juego |
| `champions` | 40 | Clase de campeón, rol, dificultad y supuestos de selección/baneo |
| `match_objectives` | 1.800 | Dragones, Barones y torres por equipo |

### Principales dimensiones de análisis

**Rendimiento**
- Tasa de victorias
- KDA
- Participación en asesinatos
- CS/min
- Oro/min
- Daño/min
- Puntuación de visión/min
- Participación en objetivos

**Contexto**
- Rol
- Tier
- Campeón
- Clase de campeón
- Parche
- Duración de la partida
- Estilo de juego

**Engagement**
- Partidas por jugador
- Actividad mensual
- Actividad recurrente
- Intensidad de las sesiones

---

## 🔎 Preguntas analíticas

### 01 — Comportamientos asociados a la victoria

¿Qué métricas a nivel de jugador presentan una mayor asociación con el resultado de la partida?

### 02 — Rendimiento de los jugadores

¿Qué jugadores presentan un rendimiento consistentemente superior o inferior respecto de su grupo de comparación?

### 03 — Análisis de campeones

¿Cómo interactúan el rol, la dificultad, el tamaño de la muestra y la tasa de victorias de cada campeón?

### 04 — Impacto de los objetivos

¿La participación en objetivos está asociada con la victoria después de considerar el rol y el contexto de la partida?

### 05 — Engagement

¿Qué señales de comportamiento podrían indicar cambios en la actividad de los jugadores?

---

## 🧪 Calidad de los datos

La calidad de los datos se considera una parte fundamental del análisis y no una etapa posterior.

El proyecto incluye validaciones automatizadas para detectar:

- registros duplicados
- valores nulos
- indicadores de victoria inválidos
- duraciones imposibles
- valores K/D/A inválidos
- cantidad incorrecta de participantes
- problemas de integridad referencial
- inconsistencias entre campeones y jugadores
- inconsistencias en los objetivos

Las validaciones de calidad deben ejecutarse antes de utilizar los datos para el Dashboard.

Los resultados se documentan en:

`docs/data_quality_results.csv`

---

## 🐍 Análisis con Python

Notebook principal:

`notebooks/01_analysis_template.ipynb`

El notebook está estructurado en las siguientes etapas:

1. Carga de datos
2. Validación de datos
3. Limpieza
4. Creación de variables
5. Estadística descriptiva
6. Análisis exploratorio
7. Segmentación de jugadores
8. Análisis de campeones y roles
9. Análisis de objetivos
10. Análisis estadístico
11. Interpretación de resultados desde una perspectiva de negocio

El objetivo es mantener un análisis **reproducible, explicable y basado en datos**.

---

## 🗄️ Análisis con SQL

Archivo SQL principal:

`sql/analysis.sql`

Las consultas abarcan:

- extracción de KPI
- rankings de jugadores
- rendimiento por campeón
- comparación entre roles
- análisis de objetivos
- tendencias temporales
- lógica de agregación

SQL se utiliza para demostrar que el análisis puede realizarse directamente desde la capa de datos y no únicamente desde Python.

---

## 📈 Dashboard

La capa de Business Intelligence está planificada en cuatro vistas principales:

### Resumen Ejecutivo

- Tasa de victorias
- MMR promedio
- Cantidad de partidas
- KDA promedio
- Control de objetivos
- Evolución del rendimiento

### Rendimiento de Jugadores

- Ranking de jugadores
- Tasa de victorias
- KDA
- CS/min
- Visión
- Participación en objetivos
- Segmentación de rendimiento

### Inteligencia de Campeones

- Tasa de selección
- Tasa de victorias
- Rol
- Tamaño de muestra
- Dificultad
- Variabilidad del rendimiento

### Engagement

- Jugadores activos
- Partidas por jugador
- Actividad mensual
- Tasa de jugadores recurrentes
- Señales de actividad

Especificación del Dashboard:

`dashboard/dashboard_spec.md`

> Agregar las capturas finales de Power BI/Tableau en `images/` e incorporarlas aquí una vez finalizado el Dashboard.

---

## 💡 Del KPI a la decisión de negocio

Un proyecto de Analytics sólido debe conectar los principales hallazgos con posibles acciones.

Ejemplo de framework:

| Hallazgo | Evidencia | Acción potencial | Métrica de éxito |
|---|---|---|---|
| Una mayor participación en objetivos está asociada con una mayor tasa de victorias | Comparación entre grupos + tamaño de muestra | Feedback enfocado en objetivos | Participación en objetivos |
| Algunos jugadores superan consistentemente a su grupo de comparación | KPI normalizados respecto al grupo | Feedback personalizado de rendimiento | Consistencia del rendimiento |
| Determinadas combinaciones de campeón/rol presentan diferentes resultados | Análisis de campeones ajustado por rol | Mejorar recomendaciones | Tasa de victorias / adopción |

**Importante:** un análisis observacional no demuestra causalidad. Por lo tanto, los hallazgos deben describirse como asociaciones, salvo que se realice un experimento causal.

---

## 🧱 Arquitectura del proyecto

```text
soloq-analytics-portfolio/
│
├── data/
│   └── raw/
│       ├── matches.csv
│       ├── match_participants.csv
│       ├── players.csv
│       ├── champions.csv
│       └── match_objectives.csv
│
├── dashboard/
│   └── dashboard_spec.md
│
├── docs/
│   ├── business_case.md
│   ├── data_dictionary.md
│   ├── methodology.md
│   └── data_quality_results.csv
│
├── images/
│   └── capturas del Dashboard
│
├── notebooks/
│   └── 01_analysis_template.ipynb
│
├── sql/
│   └── analysis.sql
│
├── src/
│   ├── generate_data.py
│   └── data_quality.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
