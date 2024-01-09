export default function createInt8TypedArray(length, position, value) {
  if (length < position) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const dataView1 = new DataView(buffer);
  dataView1.setInt8(position, value);
  return dataView1;
}
