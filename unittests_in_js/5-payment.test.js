const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');
const sinon = require('sinon');


describe('test sendPaymentRequestToApi', function () {
	let spy;

	beforeEach(function () {
		spy = sinon.spy(console, 'log');
	});

	afterEach(function () {
		spy.restore();
	});

	it('validate response from console.log for value (100, 20)', function () {
		sendPaymentRequestToApi(100, 20);
		sinon.assert.calledOnce(spy);
		sinon.assert.calledWithExactly(spy, 'The total is: 120');
	});

	it('validate response from console.log for value (10, 10)', function () {
		sendPaymentRequestToApi(10, 10);
		sinon.assert.calledOnce(spy);
		sinon.assert.calledWithExactly(spy, 'The total is: 20');
	});
});
