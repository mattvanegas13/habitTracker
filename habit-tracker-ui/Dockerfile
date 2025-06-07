FROM node:18-alpine
WORKDIR /habit-tracker-ui
COPY package*.json ./
COPY next*.ts ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD [ "npm", "run", "dev" ]