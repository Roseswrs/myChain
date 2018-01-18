import socket


def is_valid_ip(ip):
    q = ip.split('.')
    return len(q) == 4 and len(list(filter(lambda x: 0 <= x <= 255, map(int, filter(lambda x: x.isdigit(), q))))) == 4


if __name__ == '__main__':
    print(is_valid_ip('1.1.1.1'))
