# Multi-stage Dockerfile for containerizing the static website
# This Dockerfile builds and serves the static website using Nginx

# Stage 1: Builder Stage - Node.js
FROM node:20-alpine as builder
# Set working directory for the build stage
WORKDIR /app
# Copy package.json and package-lock.json 
COPY package*.json ./
# Install Node dependencies
RUN npm ci --omit=optional
# Copy the entire project source code
COPY . .

# Stage 2: Runtime Stage - Nginx Web Server
FROM nginx:alpine
# Set labels for metadata information
LABEL maintainer="JDevOps2025"
LABEL description="Static website container for JDevOps Software Engineering project"
LABEL version="1.0"
# Install curl for health checks
RUN apk add --no-cache curl
# Copy custom Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf
# Copy the static website files from the builder stage into Nginx's document root
# The static/ folder contains all HTML, CSS, JS, images, and other assets
COPY static/ /usr/share/nginx/html/
# Set proper permissions for Nginx to serve the files
RUN chmod -R 755 /usr/share/nginx/html/
# Expose port 80 for HTTP traffic
EXPOSE 80
# Health check to verify the container is running correctly
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1
# Start Nginx
# This command runs Nginx with the "-g daemon off;" this is necessary for Docker containers to keep running
CMD ["nginx", "-g", "daemon off;"]