FROM nginx:stable-alpine

COPY nginx/ssl/* /etc/ssl

RUN rm /etc/nginx/conf.d/default.conf
RUN touch /etc/sysctl.conf
RUN echo net.ipv4.ip_unprivileged_port_start=80 > /etc/sysctl.conf

COPY nginx/nginx.conf /etc/nginx/conf.d/
