const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const resultOfSum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${resultOfSum}`);
};
module.exports = sendPaymentRequestToApi;
