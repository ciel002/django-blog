import redis

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, password='123456', max_connections=10)


# conn = redis.StrictRedis(connection_pool=POOL)

def get_redis():
    return redis.StrictRedis(connection_pool=POOL)
