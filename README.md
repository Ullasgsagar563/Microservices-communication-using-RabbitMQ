# Inventory Management System with RabbitMQ

## Description
This project is an Inventory Management System developed using microservices architecture. It leverages RabbitMQ for inter-service communication, ensuring reliable message handling between various components, including producers and consumers. The system is containerized using Docker, allowing for easy deployment and scalability.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Outcome](#outcome)
- [License](#license)

## Technologies Used
- **RabbitMQ**: A message broker for handling communication between services.
- **Docker**: For containerizing the microservices.
- **Python**: The primary programming language for service development.
- **MongoDB**: Used for data storage (if applicable).

## Project Structure
The project follows a modular structure with individual folders for each service:

```plaintext
<project-directory>
│
├── docker-compose.yml
│
├── producer
│   ├── producer.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── consumer_one
│   ├── healthcheck.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── consumer_two
│   ├── item_creation.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── consumer_three
│   ├── stock_management.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── consumer_four
│   ├── order_processing.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── database_service
    ├── Dockerfile
    └── requirements.txt
```

## Setup Instructions
Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Ensure that Docker and Docker Compose are installed on your machine.

3. Build and run the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Access the RabbitMQ management interface by navigating to [http://localhost:15672](http://localhost:15672) in your web browser (default username/password: `guest`/`guest`).

## Usage
- **Producer**: Sends messages related to inventory updates.
- **Consumer 1**: Monitors health checks and handles message consumption.
- **Consumer 2**: Responsible for creating items in the inventory.
- **Consumer 3**: Manages stock levels.
- **Consumer 4**: Processes orders and updates inventory accordingly.

Each service can be tested independently by checking the logs for successful message consumption.

## Outcome
This project demonstrates the power of microservices architecture, achieving decoupled services that communicate efficiently through RabbitMQ. The use of Docker ensures that the services can be easily deployed and scaled, improving overall system reliability and performance.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
