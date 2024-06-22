const Utils = require('./utils.js');

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
    const resultOfSum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${resultOfSum}`);
    return resultOfSum;
}
module.exports = sendPaymentRequestToApi;
