const sendPaymentRequestToApi = require('./4-payment');
const sinon = require('sinon');
const Utils = require('./utils');
const chai = require('chai');

describe('sendPaymentRequestToApi', () => {
    const consoleLogSpy = sinon.spy(console, 'log');

    it('stubs Utils calculateNumber usage', () => {
        const stubsUtils = sinon.stub(Utils, 'calculateNumber');
        stubsUtils.withArgs('SUM', 100, 20).returns(10);
        sendPaymentRequestToApi(100, 20);
        chai.expect(consoleLogSpy.calledOnce).to.be.true;
        chai.expect(consoleLogSpy.calledWith('The total is: 10')).to.be.true;
        stubsUtils.restore();
        consoleLogSpy.restore();
    });
});
