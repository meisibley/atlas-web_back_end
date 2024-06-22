const sendPaymentRequestToApi = require('./3-payment');
const sinon = require('sinon');
const Utils = require('./utils');
//const { expect } = require('chai');

// describe('sendPaymentRequestToApi', () => {
//     const sendPaymentSpy = sinon.spy(sendPaymentRequestToApi);
//     const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
//     const consoleLogSpy = sinon.spy(console, 'log');

//     const totalAmount = sendPaymentRequestToApi(100, 20);

//     it('valid if sendPaymentRequestToApi received correct inputs', () => {
//         expect(sendPaymentSpy.calledWithExactly(100, 20));
//     });
//     it('valid if calculateNumber received correct inputs', () => {
//         expect(calculateNumberSpy.calledWithExactly('SUM', 100, 20));
//     });
//     it('valid totalAmount value returned from sendPaymentRequestToApi', () => {
//         expect(totalAmount).to.be.equal(120);
//     });
//     it('valid if console.log executed and printed correct string', () => {
//         expect(consoleLogSpy.calledWithExactly('The total is: 120'));
//     });
// });
describe('sendPaymentRequestAPI', function() {
    afterEach(function() {
      sinon.restore();
    })
  
      it('calls the CalculateNumber with correct args SUM whole', () => {
          const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  
          sendPaymentRequestToApi(100, 20);
          sinon.assert.calledOnce(calculateNumberSpy);
          sinon.assert.calledOnceWithExactly(calculateNumberSpy, 'SUM', 100, 20);
      });
  
      it('calls the CalculateNumber with correct args SUM float', () => {
          const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  
          sendPaymentRequestToApi(100.2, 20);
          sinon.assert.calledOnce(calculateNumberSpy);
          sinon.assert.calledOnceWithExactly(calculateNumberSpy, 'SUM', 100.2, 20);
      });
      it('calls the CalculateNumber with correct args SUM float and 0', () => {
          const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  
          sendPaymentRequestToApi(1.3, 0);
          sinon.assert.calledOnce(calculateNumberSpy);
          sinon.assert.calledOnceWithExactly(calculateNumberSpy, 'SUM', 1.3, 0);
      });
      it('calls the CalculateNumber with correct args SUM float over .5 and 0', () => {
          const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  
          sendPaymentRequestToApi(1.7, 0);
          sinon.assert.calledOnce(calculateNumberSpy);
          sinon.assert.calledOnceWithExactly(calculateNumberSpy, 'SUM', 1.7, 0);
      });
      it('calls the CalculateNumber with correct args SUM floats over .5', () => {
          const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  
          sendPaymentRequestToApi(1.6, 1.8);
          sinon.assert.calledOnce(calculateNumberSpy);
          sinon.assert.calledOnceWithExactly(calculateNumberSpy, 'SUM', 1.6, 1.8);
      });
      it('calls the CalculateNumber with correct args SUM floats over .5 and under .5', () => {
          const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
  
          sendPaymentRequestToApi(1.7, 1.2);
          sinon.assert.calledOnce(calculateNumberSpy);
          sinon.assert.calledOnceWithExactly(calculateNumberSpy, 'SUM', 1.7, 1.2);
      });
  
      it('Displays the console message', () => {
          const consoleMsg = sinon.spy(console, 'log');
      
          sendPaymentRequestToApi(100, 20);
          sinon.assert.calledOnce(consoleMsg);
          sinon.assert.calledOnceWithExactly(consoleMsg, 'The total is: 120');
      });
  });
