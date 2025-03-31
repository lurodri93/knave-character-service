# Knave Character Creator Microservice

Este microservicio genera un personaje aleatorio de Knave y devuelve su información como JSON.

## Endpoint

**POST /create-character**

### Body
```json
{
  "player_id": "nombre_opcional"
}
```

### Respuesta
```json
{
  "name": "...",
  "level": 1,
  "xp": "0/500",
  "hit_points": 6,
  "stats": {...},
  "inventory": {...},
  "traits": {...}
}
```

## Despliegue en Heroku

```bash
heroku create knave-character
git push heroku main
```
