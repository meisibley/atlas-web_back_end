const listProducts = [
    {
      id: 1,
      name: 'Suitcase 250',
      price: 50,
      stock: 4
    },
    {
      id: 2,
      name: 'Suitcase 450',
      price: 100,
      stock: 10
    },
    {
      id: 3,
      name: 'Suitcase 650',
      price: 350,
      stock: 2
    },
    {
      id: 4,
      name: 'Suitcase 1050',
      price: 550,
      stock: 5
    }
  ]
  function getItemById(id) {
    return listProducts.find(item => item.id == id)
  }
  
  const express = require('express');
  const app = express();
  const port = 1245;
  
  app.get('/list_products', (req, res) => {
    const products = listProducts.map(product => ({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock
    }));
    res.send(JSON.stringify(products));
  });
  
  app.get('/list_products/:itemId', async (req, res) => {
    const stockId = req.params.itemId
    const product = getItemById(stockId);
    if (!product) {
      res.json({status: "Product not found"})
    }
    const currentQuanity = await getCurrentReservedStockById(itemId) ?? product.stock;
    res.json({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuanity: currentQuanity
    })
  })
  
  app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
  });
  
  import redis from 'redis';
  const { promisify } = require('util');
  
  const client = redis.createClient();
  const setAsync = promisify(client.set).bind(client);
  const getAsync = promisify(client.get).bind(client);
  
  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });
  
  client.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
  });
  
  async function reserveStockById(itemId, stock) {
    await setAsync(`item:${itemId}`, stock);
  }
  
  async function getCurrentReservedStockById(itemId) {
    const reservedStock = await getAsync(`item:${itemId}`);
    return parseInt(reservedStock) || null;
  }
  