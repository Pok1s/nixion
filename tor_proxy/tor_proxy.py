# tor_proxy.py
import socks
import socket

def setup_tor_proxy():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket

# Example usage
if __name__ == "__main__":
    setup_tor_proxy()
    # Now all outgoing connections will use Tor
    import requests
    response = requests.get('http://example.com')
    print(response.text)
