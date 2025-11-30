# JDevOps Software Engineering - Static Website with Docker & CI/CD

A production-ready static website multi-region (EU-West-1 & US-East-1) storage in S3 bucket and hosted in AWS with Docker containerization, GitHub Actions CI/CD, and comprehensive testing infrastructure.

### Website Instances

- **EU-WEST-1** - http://eu-west-1-jdevops-webpage.s3-website-eu-west-1.amazonaws.com
- **US-EAST-1** - http://us-east-1-jdevops-webpage.s3-website-us-east-1.amazonaws.com

### Run Time

```bash
# Start containerized environment
docker-compose up -d

# Visit website
# Open http://localhost:8080

# Stop services
docker-compose down
```

### Core Components

- **Static Website** - HTML, CSS, JavaScript, images
- **Nginx Server** - Lightweight Alpine-based web server
- **Docker** - Multi-stage build, optimized image
- **GitHub Actions** - Automated CI/CD pipeline
- **Testing Suite** - HTML validation, JS linting, Cypress, Selenium

### Infrastructure

- **docker-compose.yml** - Multi-container local development (web + testing)
- **Dockerfile** - Production-ready image
- **nginx.conf** - Security headers, caching, compression
- **.dockerignore** - Optimized image size

### CI/CD Pipeline

- Automated builds on push to master
- Image testing before push
- Security vulnerability scanning
- Push to GitHub Container Registry (GHCR)

## Project Structure

```
├── Dockerfile                           # Docker image definition
├── nginx.conf                           # Web server configuration
├── docker-compose.yml                   # Multi-container setup
├── .dockerignore                        # Exclude files from image
│
├── static/                              # Website source files
│   ├── index.html
│   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── ...
│
├── Tests/e2e/                          # End-to-end tests
│   └── test_homepage.py                # Selenium tests
│
├── .github/workflows/                  # GitHub Actions
│   ├── docker-build-push.yml          # Docker CI/CD workflow
│   ├── deploy-to-s3.yml               # S3 deployment
│   ├── homepage-test.yml              # Selenium tests
│   └── static-site-validation.yml     # HTML/CSS/JS validation
│
└── package.json, requirements.txt      # Dependencies
```

## Docker

### Build Image

```bash
docker build -t jdevops-website:latest.
```

### Run Container

```bash
docker run -p 8080:80 jdevops-website:latest
```

### Use Docker Compose (Recommended)

```bash
# Start all services (web + testing)
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f web

# Run tests
docker-compose exec test-web npm test
docker-compose exec test-python pytest
```

## Features

### Security

- Non-root user
- Security headers (CSP, X-Frame-Options, XSS protection)
- Blocks sensitive files (.git, .env)
- Vulnerability scanning

### Performance

- Multi-stage Docker builds
- Alpine Linux (lightweight)
- Gzip compression
- Browser caching (1 year for assets)
- Optimized image size (~50MB)

### Testing

- HTML validation (HTMLHint)
- JavaScript linting (ESLint)
- Functional tests (Cypress)
- End-to-end tests (Selenium/Pytest)

### Automation

- GitHub Actions on push
- Image testing before push
- Security scanning
- Push to GHCR
- Ready for Kubernetes

## Workflows

### Local Development

```bash
# Start services
docker-compose up -d

# Edit files in static/
# Refresh browser to see changes (volumes are mounted)

# Run tests
docker-compose exec test-web npx htmlhint ./static/**/*.html
docker-compose exec test-web npx eslint static/**/*.js

# Stop
docker-compose down
```
