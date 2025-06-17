# 🛠 Helpdesk App — Sistema de gestión de tickets técnicos

Este proyecto es un sistema de soporte interno (**helpdesk**) desarrollado con **FastAPI**, diseñado para que empleados puedan crear tickets técnicos, técnicos puedan resolverlos, y administradores gestionen el sistema.

Es una aplicación pensada como práctica profesional, modular y extensible.

---

## 🚀 Funcionalidades implementadas hasta ahora

### 👤 Autenticación
- Registro de usuarios vía `/register`
- Inicio de sesión vía `/login` con JWT
- Contraseñas hasheadas con `bcrypt`
- Tokens con expiración, generados con `python-jose`
- Middleware que protege rutas automáticamente

### 🔐 Protección de rutas
- Implementación de `get_current_user()` para verificar token
- Endpoint `/mytasks` que devuelve los datos del usuario autenticado
- Comprobación automática de token válido o vencido (`401 Unauthorized` si no se envía o es inválido)

### 🧱 Modelo de usuarios
Cada usuario tiene:
- `username`
- `email`
- `hashed_password`
- `role` (`employee`, `technician`, `admin`)

---

## 📦 Tecnologías utilizadas

- **FastAPI** — Framework backend principal
- **SQLAlchemy** — ORM para definir y consultar la base de datos
- **Alembic** — Control de versiones de la base de datos
- **JWT** — Autenticación segura con tokens
- **Docker** (en preparación)
- **PostgreSQL o SQLite** — Motor de base de datos
## 🧭 Pendientes y próximos pasos

- [ ] CRUD completo de tickets
- [ ] Endpoint para técnicos para cerrar tickets
- [ ] Filtro de tareas por usuario
- [ ] Control de acceso por rol (`admin`, `technician`, `employee`)
- [ ] Integración de análisis de texto (NLP con clasificador básico o GPT)
- [ ] Interfaz en React

