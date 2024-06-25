import { createClient } from 'redis';

const redisClient = createClient();
redisClient.on('Connected', () =>
    console.log('Redis client connected to the server'));
redisClient.on('error', (err) =>
    console.log(`Redis client not connected to the server: ${err}`));
