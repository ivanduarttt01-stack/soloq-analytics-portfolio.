# 🎮 SoloQ Pulse — Análisis Competitivo

Proyecto integral de Data Analytics para portfolio  
**Python · SQL · Power BI · Calidad de Datos · Analítica de Producto**

---

## 📌 Descripción del proyecto

**SoloQ Pulse** es un caso de estudio ficticio de Data Analytics diseñado para simular el tipo de trabajo que realiza un Data Analyst, BI Analyst o Product Analyst dentro de una plataforma de gaming competitivo.

El objetivo es desarrollar un flujo completo de análisis:
**Pregunta de negocio → Validación de datos → Transformación → Análisis con SQL/Python → KPI → Dashboard → Insight de negocio → Acción → Medición**

> ⚠️ **Aviso sobre los datos:** Todas las observaciones son sintéticas y fueron generadas específicamente para este proyecto de portfolio. No corresponden a datos de Riot Games, OP.GG ni a jugadores reales.

---

## 🎯 Problema de negocio

Un equipo de producto ficticio busca responder las siguientes preguntas utilizando evidencia basada en datos:

* ¿Qué comportamientos de los jugadores están asociados con la victoria?
* ¿Cómo se relacionan el rol, campeón y estilo de juego con el rendimiento?
* ¿Qué jugadores muestran un rendimiento consistente a lo largo del tiempo?
* ¿Qué importancia tienen los objetivos en comparación con las estadísticas de combate?
* ¿Qué métricas podrían utilizarse para mejorar el feedback posterior a las partidas y el engagement de los jugadores?

---

## 📊 Datos disponibles

| Dataset | Registros | Descripción |
| :--- | :--- | :--- |
| **matches** | 1.800 | Contexto de las partidas, duración, parche, equilibrio de MMR y resultado |
| **match_participants** | 18.000 | Métricas individuales de combate, CS, visión, oro y objetivos |
| **players** | 80 | Cuenta, tier, rol, región y atributos de estilo de juego |
| **champions** | 40 | Clase de campeón, rol, dificultad y supuestos de selección/baneo |
| **match_objectives** | 1.800 | Dragones, Barones y torres por equipo |

### Principales dimensiones de análisis
* **Rendimiento:** Tasa de victorias, KDA, Participación en asesinatos, CS/min, Oro/min, Daño/min, Puntuación de visión/min, Participación en objetivos.
* **Contexto:** Rol, Tier, Campeón, Clase de campeón, Parche, Duración de la partida.
* **Engagement:** Partidas por jugador, Actividad mensual, Actividad recurrente, Intensidad de las sesiones.

---

## 🔎 Preguntas analíticas

* **01 — Comportamientos asociados a la victoria:** ¿Qué métricas a nivel de jugador presentan una mayor asociación con el resultado de la partida?
* **02 — Rendimiento de los jugadores:** ¿Qué jugadores presentan un rendimiento consistentemente superior o inferior respecto de su grupo de comparación?
* **03 — Análisis de campeones:** ¿Cómo interactúan el rol, la dificultad, el tamaño de la muestra y la tasa de victorias de cada campeón?
* **04 — Impacto de los objetivos:** ¿La participación en objetivos está asociada con la victoria después de considerar el rol y el contexto de la partida?
* **05 — Engagement:** ¿Qué señales de comportamiento podrían indicar cambios en la actividad de los jugadores?

---

## 🧪 Calidad de los datos

La calidad de los datos es una etapa fundamental integrada desde el inicio. El proyecto incluye validaciones automatizadas para detectar:
* Registros duplicados y valores nulos.
* Indicadores de victoria y valores K/D/A inválidos.
* Duraciones de partida imposibles y cantidad incorrecta de participantes.
* Integridad referencial e inconsistencias entre campeones, jugadores y objetivos.

> 📄 **Reporte generado:** Los resultados se documentan en `docs/data_quality_results.csv`.

---

## 📈 Visualización

### Vistas principales
1. **Resumen Ejecutivo:** Tasa de victorias, MMR promedio, KDA promedio, control de objetivos y evolución del rendimiento.
2. **Rendimiento de Jugadores:** Rankings, CS/min, visión, participación en objetivos y segmentación de rendimiento.
3. **Inteligencia de Campeones:** Tasa de selección y victoria, interacción con roles, dificultad y variabilidad.
4. **Engagement:** Jugadores activos, partidas por usuario, actividad mensual y tasa de recurrencia.

📌 *Especificación detallada del diseño disponible en: [`dashboard/dashboard_spec.md`](dashboard/dashboard_spec.md)*

---

## 📌 Hallazgos e Insights de Negocio

* **Impacto de Objetivos:** Los equipos con una participación en objetivos superiores al 60% incrementan su tasa de victorias de forma significativa frente a los orientados únicamente a asesinatos (*kills*).
* **Eficiencia de Visión:** Mantener una puntuación de visión/min constante en fases tempranas muestra una alta correlación positiva con la conversión de partidas en rangos altos (Tier Platino+).
* **Consistencia sobre Pico:** La baja variabilidad en el rendimiento individual predice mejor el ascenso de MMR que picos aislados de alto KDA.

---

## 💡 Del KPI a la decisión de negocio

| Hallazgo | Evidencia | Acción potencial | Métrica de éxito |
| :--- | :--- | :--- | :--- |
| **Mayor participación en objetivos asociada a la victoria** | Comparación entre grupos + tamaño de muestra | Implementar feedback enfocado en objetivos pre-partida | % Participación en objetivos |
| **Jugadores superan consistentemente a su grupo** | KPI normalizados respecto al grupo de comparación | Sistema de feedback y coaching personalizado de rendimiento | Consistencia del rendimiento |
| **Variación de resultados según combinación campeón/rol** | Análisis de campeones ajustado por rol | Mejorar la recomendación de campeones en selección | Tasa de victorias / Adopción |

> ⚠️ *Nota:* Un análisis observacional muestra asociaciones, no causalidad directa.

---

## 🐍 Análisis con Python & 🗄️ SQL

* **Python Notebook:** [`notebooks/01_analysis_template.ipynb`](notebooks/01_analysis_template.ipynb)
  *(Carga, limpieza, ingeniería de variables, segmentación, análisis estadístico e interpretación).*
* **Consultas SQL:** [`sql/analysis.sql`](sql/analysis.sql)
  *(Extracción de KPI, rankings, rendimiento por campeón, tendencias y agregaciones desde la capa de datos).*

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
│   └── dashboard_preview.png
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
