FROM node:18-alpine

WORKDIR /app

# Install serve globally first
RUN npm install -g serve

# Copy package files from frontend directory
COPY frontend/package.json frontend/yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy all frontend source code
COPY frontend/ .

# Build the app
RUN yarn build

# Expose port
EXPOSE 3000

# Serve the app
CMD ["serve", "-s", "build", "-l", "3000"]
