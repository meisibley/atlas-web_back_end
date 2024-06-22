const Utils = require('./utils');

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
    const resultOfSum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${resultOfSum}`);
    return resultOfSum;
};
module.exports = sendPaymentRequestToApi;
