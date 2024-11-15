# Usa una imagen base de Alpine Linux
FROM alpine:latest

# Instala SQLite
RUN apk update && apk add sqlite

# Crea un directorio para la base de datos
RUN mkdir /data

# Define el directorio de trabajo
WORKDIR /data

# Comando por defecto al iniciar el contenedor
CMD ["sqlite3", "/data/database.db"]
