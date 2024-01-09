export default function updateUniqueItems(map) {
  if (!Map.isMap(map)) {
    throw new Error('Cannot process');
  }

  for (const [name, quantity] of map.entries()) {
    if (quantity === 1) {
      map.set(name, 100);
    }
  }
  return map;
}
