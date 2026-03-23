# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. Students will implement CRUD endpoints, define request/response models with Pydantic, and test the API locally.

## 📝 Tasks

### 🛠️ API Implementation

#### Description

Create a FastAPI application that exposes endpoints to create, read, update, and delete items. Use Pydantic models for request validation and an in-memory data store for persistence during runtime.

#### Requirements
Completed program should:

- Expose REST endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- Use Pydantic models for request/response validation
- Handle not-found and bad-request errors with proper HTTP status codes
- Include clear run instructions and an example in the `starter-code.py`

### 🛠️ Testing and Extras

#### Description

Verify the API works by running it locally and using `curl` or a tool like `httpie`/Postman.

#### Requirements
Completed program may include:

- Example requests and responses
- Case-insensitive input validation where appropriate
- Optional persistence to a JSON file for longer-lived state

---

### Starter files

- `starter-code.py` — minimal FastAPI app to get started
- `requirements.txt` — packages needed to run the app
