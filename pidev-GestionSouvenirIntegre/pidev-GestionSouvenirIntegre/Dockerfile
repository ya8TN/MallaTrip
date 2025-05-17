FROM eclipse-temurin:17-jdk AS build
WORKDIR /app
RUN apt-get update && apt-get install -y dos2unix
COPY pom.xml mvnw ./
COPY .mvn ./.mvn
RUN dos2unix mvnw && chmod +x mvnw
COPY src ./src
RUN ./mvnw clean package -DskipTests


FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8089
ENV SPRING_DATASOURCE_URL=jdbc:mysql://db:3306/tourisme1?createDatabaseIfNotExist=true \
    SPRING_DATASOURCE_USERNAME=root \
    SPRING_DATASOURCE_PASSWORD= \
    SERVER_PORT=8089 \
    SERVER_SERVLET_CONTEXT_PATH=/tourisme
ENTRYPOINT ["java", "-Djava.net.preferIPv4Stack=true", "-jar", "app.jar"]