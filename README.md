# Umbra AI Evaluator

Microservicio REST desarrollado en Python (FastAPI) con un pipeline de Integración y Despliegue Continuo (CI/CD) que aplica inteligencia artificial para la validación estática y el aseguramiento de la calidad del software (SQA).

## Características Principales
- **API RESTful:** Desarrollada con FastAPI y Pydantic.
- **Métricas de Producto:** Cálculo automático de densidad de defectos y cobertura de código.
- **DevOps y CI/CD:** Pipeline automatizado mediante GitHub Actions.
- **Validación Asistida:** Script de evaluación que simula un agente de IA para aprobar o rechazar pases a producción.
- **Contenedorización:** Despliegue inmutable mediante Docker.

## Estructura del Proyecto
* `/app`: Código fuente del microservicio.
* `/tests`: Pruebas unitarias automatizadas con Pytest.
* `/scripts`: Agentes de evaluación y scripts de integración CI/CD.
* `.github/workflows`: Definición del pipeline automatizado.

## Ejecución Local (Desarrollo)

1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   # En Windows: venv\Scripts\activate
   # En Linux: source venv/bin/activate