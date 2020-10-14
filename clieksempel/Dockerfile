FROM node:alpine
COPY package*.json app.js ./
RUN npm install --production
CMD ["node", "app.js"]