export default function updateUniqueItems(groceryMap) {
  if (!(groceryMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [name, quantity] of groceryMap.entries()) {
    if (quantity === 1) groceryMap.set(name, 100);
  }
  return groceryMap;
}
