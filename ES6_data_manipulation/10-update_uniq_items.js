import groceriesList from './9-groceries_list';

export default function updateUniqueItems(groceryMap) {
  if (!Map.isMap(groceryMap)) {
    throw new Error('Cannot process');
  }

  const updatedMap = groceryMap.forEach((element) => {
    if (element.quantity === 1) {
      element.quantity *= 100;
    }
  });
  return updatedMap;
}
