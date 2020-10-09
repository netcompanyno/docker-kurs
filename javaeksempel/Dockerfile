FROM openjdk:11-jre-slim

ENV TZ=Europe/Oslo

ARG JAR_FILE

COPY target/${JAR_FILE} app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app.jar"]
