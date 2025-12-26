FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

ARG GIT_SHA=unknown

COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/

RUN sed -i "s/LOCAL-DEV/${GIT_SHA}/g" /usr/share/nginx/html/index.html

EXPOSE 80
