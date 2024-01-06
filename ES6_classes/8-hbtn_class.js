export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size !== 'number') {
      throw TypeError('Size must be a number');
    }
    this._size = size;
    if (typeof location !== 'string') {
      throw TypeError('Location must be a string');
    }
    this._location = location;
  }

  [Symbol.toPrimitive](inputValue) {
    if (inputValue === 'number') {
      return this._size;
    }
    return this._location;
  }
}
