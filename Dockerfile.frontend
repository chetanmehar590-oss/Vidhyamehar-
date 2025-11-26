FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files from frontend directory
COPY frontend/package.json frontend/yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy all frontend source code
COPY frontend/ .

# Build the app
RUN yarn build

# Production stage
FROM node:18-alpine

WORKDIR /app

# Install serve globally
RUN yarn global add serve

# Copy build from builder
COPY --from=builder /app/build ./build

# Expose port
EXPOSE 3000

# Serve the app
CMD ["serve", "-s", "build", "-l", "3000"]
