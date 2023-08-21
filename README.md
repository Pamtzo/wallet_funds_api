# Wallet Balance API

This FastAPI-based API retrieves and manages wallet balance information from a blockchain network, specifically for the Ethereum cryptocurrency. It fetches wallet balances, their historical data, and stores them in a MongoDB database.

## Prerequisites

- Docker
- Docker Compose

## Usage

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Environment Configuration:**

   Modify the `.env` file in the root directory with your desired environment variables.

3. **Run the Application:**

   Execute the following command to start the application using `docker-compose`:

   ```bash
   docker-compose up
   ```

4. **Access the API:**

   Once the application is running, you can access the API at `http://localhost:8000`.

   - To get the wallet balance and save it to the database:  
     Endpoint: `/wallet/balance/`  
     Method: GET  
     Query Parameter: `wallet` (Ethereum wallet address)

   - To get the historical wallet data from the database:  
     Endpoint: `/wallet/history/`  
     Method: GET  
     Query Parameter: `wallet` (Ethereum wallet address)

## Docker Compose Configuration

The `docker-compose.yml` file in the root directory is pre-configured to set up the MongoDB instance and the FastAPI application within separate Docker containers.

## Dependencies

- FastAPI
- Web3.py
- Motor
- Pydantic
- ...
