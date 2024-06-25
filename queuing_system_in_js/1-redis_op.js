import { createClient } from 'redis';

const redisClient = createClient();
const redis = require('redis');

redisClient.on('Connected', () =>
    console.log('Redis client connected to the server'));
redisClient.on('error', (err) =>
    console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => {
    redisClient.set(schoolName, value, redis.print);
};
const displaySchoolValue = (schoolName) => {
    redisClient.get(schoolName, (err, value) => console.log(value));
};
   
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
