import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw TypeError('Amount must be a number');
    }
    this._amount = amount;
    if (!(currency instanceof Currency)) {
      throw TypeError('Currency must be type of Currency');
    }
    this._currency = currency;
  }

  set amount(inputAmount) {
    if (typeof inputAmount !== 'number') {
      throw TypeError('Amount must be a number');
    }
    this._amount = amount;
  }

  get amount() {
    return this._amount;
  }

  set currency(inputCurrency) {
    if (!(inputCurrency instanceof Currency)) {
      throw TypeError('Currency must be type of Currency');
    }
    this._currency = inputCurrency;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    const disPrice = new Currency(this._currency.code, this._currency.name);
    return `${this._amount} ${disPrice.name} (${disPrice.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if ((typeof amount !== 'number') || (typeof conversionRate !== 'number')) {
      throw TypeError('Both amount and conversionRate must be number');
    }
    return (amount * conversionRate);
  }
}
