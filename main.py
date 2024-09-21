import logging
from blockchain.blockchain import Blockchain
from tor_proxy.tor_proxy import setup_tor_proxy
from scaling.scaling import AutoScaler
from ai_optimizer.ai_optimizer import AINetworkOptimizer

# Налаштування логування
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Ініціалізація блокчейну
        blockchain = Blockchain()
        logging.info("Blockchain initialized.")
        
        # Налаштування Tor проксі
        setup_tor_proxy()
        logging.info("Tor proxy setup.")
        
        # Ініціалізація авто-скейлера
        scaler = AutoScaler()
        logging.info("Auto-scaling started.")
        
        # Ініціалізація AI оптимізатора
        optimizer = AINetworkOptimizer()
        
        # Приклад даних для тренування AI оптимізатора
        data = [[1, 2], [2, 3], [1, 1], [10, 10]]
        optimizer.train(data)
        logging.info("AI optimization model trained.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
