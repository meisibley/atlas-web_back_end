export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw TypeError('Code must be a string');
    }
    this._code = code;
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = name;
  }

  set code(inputCode) {
    if (typeof inputCode !== 'string') {
      throw TypeError('Code must be a string');
    }
    this._code = inputCode;
  }

  get code() {
    return this._code;
  }

  set name(inputName) {
    if (typeof inputName !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = inputName;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return this._name + "(" + this._code + ")";
  }
}
