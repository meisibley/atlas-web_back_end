export default function appendToEachArrayValue(array, appendString) {
  var idx = 0;
  for (var value of array) {
    array[idx] = appendString + value;
    idx += 1;
  }

  return array;
}
