export default function updateUniqueItems(groceryMap) {
  if (!Map.isMap(groceryMap)) {
    throw new Error('Cannot process');
  }

  const updatedMap = groceryMap.forEach((name, quantity) => {
    if (quantity === 1) {
      groceryMap.set(name, 100);
    }
  });
  return updatedMap;
}
