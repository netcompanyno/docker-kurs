FROM node:alpine

WORKDIR /app

COPY app.js package.json package-lock.json index.html ./

COPY ./public ./public

RUN npm install

USER node

EXPOSE 3000

CMD ["npm", "start"]
