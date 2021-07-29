FROM node:latest as build-stage

WORKDIR /client

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# production stage
FROM nginx:stable-alpine
# remove the default conf
RUN rm /etc/nginx/conf.d/default.conf

#  copy the nginx.conf in our filesystem into the image filesystem
COPY nginx.conf /etc/nginx/conf.d

COPY --from=build-stage /client/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]