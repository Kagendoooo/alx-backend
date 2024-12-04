import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

const hashKey = 'HolbertonSchools';
const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

Object.entries(schools).forEach(([field, value]) => {
  client.hset(hashKey, field, value, print);
});

client.hgetall(hashKey, (err, reply) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(reply);
});
