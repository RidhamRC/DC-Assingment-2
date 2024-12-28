# Use the Node.js image for building React
FROM node:16 AS build

# Set working directory
WORKDIR /app

# Copy the frontend files
COPY . .

# Install dependencies and build the project
RUN npm install
RUN npm run build

# Use NGINX to serve the built files
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Expose the NGINX port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
