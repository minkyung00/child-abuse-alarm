FROM node:16.13.1 as build-stage

WORKDIR /app
COPY package*.json ./
RUN npm install -g npm@8.1.2
COPY . .
RUN npm run build

From nginx:stable-alpine as production-stage

COPY nginx.conf /etc/nginx/nginx.conf
RUN rm -rf /usr/share/nginx/html/*

COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]