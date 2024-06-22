const request = require('request');
const { expect } = require('chai');

describe('Basic Integration Testing', () => {
    describe('GET /', () => {
        it('endpoint GET /', (done) => {
            const call = {
                url: 'http://localhost:7865',
                method: 'GET',
            };
            request(call, (error, response, body) => {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Welcome to the payment system');
                done();
            });
        });
    });
});

describe('Regex integration testing', () => {
    describe('GET /cart/:id', () => {
        it('endpoint GET /cart/:id', (done) => {
            const call = {
                url: 'http://localhost:7865/cart/12',
                method: 'GET',
            };
            request(call, (error, response, body) => {
                expect(response.statusCode).to.equal(200);
                expect(body).to.equal('Payment methods for cart 12');
                done();
            });
        });
    });
    describe('GET /cart/:isNaN', () => {
        it('endpoint: GET /cart/:isNaN', (done) => {
            const call = {
                url: 'http://localhost:7865/cart/anything',
                method: 'GET',
            };
            request(call, (error, response, body) => {
                expect(response.statusCode).to.equal(404);
                done();
            });
        });
    });
});
