
from telegram_sleuth import Sleuth
import time
sleuth = Sleuth(
    api_id='28787248', 
    api_hash='1b49dae3299b305ca08f729bc99d8e54',
    username='Nitin',
    start_date='2024-05-03',
    end_date='2024-05-05',
    download_path=r'C:\Users\nitin\Downloads', 
    print_to_console=True
)
time.sleep(10)
data = sleuth.dig()
print(data)
#sleuth.export_to_csv('name.csv')















'''
Public keys:
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g
5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO
62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/
+aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9
t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs
5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB
-----END RSA PUBLIC KEY-----'''

'''
Production configuration:
149.154.167.50:443
'''


'''
Test configuration:
149.154.167.40:443
'''