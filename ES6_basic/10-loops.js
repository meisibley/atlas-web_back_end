export default function appendToEachArrayValue(array, appendString) {
  const updatedArr = [];
  for (const value of array) {
    updatedArr.push(appendString + value);
  }

  return updatedArr;
}
