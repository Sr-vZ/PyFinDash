# Use a base image with Node.js installed
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the React app code to the container
COPY /frontend /app/

# Set the environment variable for the backend API URL
ENV REACT_APP_BACKEND_URL=http://localhost:8000

# Build the React app
RUN npm run build

# Use a minimal Nginx image as the base for serving the React app
FROM nginx:alpine

# Copy the built React app from the previous stage to the Nginx image
COPY --from=0 /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 8080

# Start Nginx to serve the React app
CMD ["nginx", "-g", "daemon off;"]