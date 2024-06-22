const sendPaymentRequestToApi = require('./3-payment.js');
const sinon = require('sinon');
const Utils = require('./utils');
const { expect } = require('chai');

describe('sendPaymentRequestToApi', () => {
    const sendPaymentSpy = sinon.spy(sendPaymentRequestToApi);
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    const consoleLogSpy = sinon.spy(console, 'log');

    const totalAmount = sendPaymentRequestToApi(100, 20);

    it('valid if sendPaymentRequestToApi received correct inputs', () => {
        expect(sendPaymentSpy.calledWithExactly(100, 20));
    });
    it('valid if calculateNumber received correct inputs', () => {
        expect(calculateNumberSpy.calledWithExactly('SUM', 100, 20));
    });
    it('valid totalAmount value returned from sendPaymentRequestToApi', () => {
        expect(totalAmount).to.be.equal(120);
    });
    it('valid if console.log executed and printed correct string', () => {
        expect(consoleLogSpy.calledWithExactly('The total is: 120'));
    });
});
