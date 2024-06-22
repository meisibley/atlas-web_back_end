const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');


describe('Test suite', function () {
	let consoleSpy;

	beforeEach(function () {
		consoleSpy = sinon.consoleSpy(console, 'log');
	});

	afterEach(function () {
		consoleSpy.restore();
	});

	it('validate response from console.log for value (100, 20)', function () {
		sendPaymentRequestToApi(100, 20);
		expect(consoleSpy.calledWith('The total is: 120')).to.be.true;
		expect(consoleSpy.calledOnce).to.be.true;
	});

	it('validate response from console.log for value (10, 10)', function () {
		sendPaymentRequestToApi(10, 10);
		expect(consoleSpy.calledWith('The total is: 20')).to.be.true;
		expect(consoleSpy.calledOnce).to.be.true;
	});
})
