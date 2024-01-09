export default function updateUniqueItems(groceryMap) {
  if (!Map.isMap(groceryMap)) {
    throw new Error('Cannot process');
  }

  for (const [key, value] of groceryMap.entries()) {
    if (value === 1) groceryMap.set(key, 100);
  }
  return groceryMap;
}
