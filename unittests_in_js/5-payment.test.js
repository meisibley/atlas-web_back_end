const sendPaymentRequestToApi = require('./5-payment');
const sinon = require('sinon');
const Utils = require('./utils');
const chai = require('chai');

describe('test sendPaymentRequestToAPI', function () {
    let consoleSpy;

    beforeEach(function () {
        consoleSpy = sinon.spy(console, 'log');
    });
    afterEach(function () {
        consoleSpy.restore();
    });

    it('validate sendPaymentRequestToAPI with value (100, 20)', function () {
        sendPaymentRequestToApi(100, 20);
        chai.expect(consoleSpy.calledWithExactly('The total is: 120')).to.be.true;
        chai.expect(consoleSpy.calledOnce).to.be.true;
    });
    it('validate sendPaymentRequestToAPI with value (10, 10)', function () {
        sendPaymentRequestToApi(10, 10);
        chai.expect(consoleSpy.calledWithExactly('The total is 20')).to.be.true;
        chai.expect(consoleSpy.calledOnce).to.be.true;
    });
});
