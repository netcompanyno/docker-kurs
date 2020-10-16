FROM node:alpine

WORKDIR /app

COPY app.js package.json package-lock.json index.html ./


RUN npm install

USER node

EXPOSE 3000

CMD ["npm", "start"]
