export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw TypeError('sqft must be a number');
    }
    if (!this.evacuationWarningMessage && this.constructor !== Building) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  set sqft(inputSqft) {
    if (typeof inputSqft !== 'number') {
      throw TypeError('sqft must be a number');
    }
    this._sqft = inputSqft;
  }

  get sqft() {
    return this._sqft;
  }
}
