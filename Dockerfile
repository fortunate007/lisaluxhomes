FROM alpine:3.20
ARG PB_VERSION=0.22.27
RUN apk add --no-cache unzip ca-certificates
ADD https://github.com/pocketbase/pocketbase/releases/download/v${PB_VERSION}/pocketbase_${PB_VERSION}_linux_amd64.zip /tmp/pb.zip
RUN unzip /tmp/pb.zip -d /pb/ && rm /tmp/pb.zip && chmod +x /pb/pocketbase
COPY pb_migrations /pb/pb_migrations
COPY pb_public /pb/pb_public
CMD /pb/pocketbase serve --http=0.0.0.0:${PORT:-10000} --dir=/data --publicDir=/pb/pb_public --migrationsDir=/pb/pb_migrations

