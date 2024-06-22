const chai = require('chai');
const request = require('request');

describe('Deep equality & Post integration testing', () => {

  it('non / endpoint', function (done) {
    request('http://localhost:7865', function (error, response, body) {
      chai.expect(body).to.equal('Welcome to the payment system');
      chai.expect(response.statusCode).to.equal(200);
      done();
    });
  });
  it('endpoint', function (done) {
    request('http://localhost:7865/', function (error, response, body) {
      chai.expect(body).to.equal('Welcome to the payment system');
      chai.expect(response.statusCode).to.equal(200);
      done();
    });
  });
  it('valid int id', function (done) {
    request('http://localhost:7865/cart/20', function (error, response, body) {
      chai.expect(body).to.equal('Payment methods for cart 20');
      chai.expect(response.statusCode).to.equal(200);
      done();
    })
  })
  it('invalid int id', function (done) {
    request('http://localhost:7865/cart/hello', function(error, response, body) {
      chai.expect(response.statusCode).to.equal(404);
      done();
    })
  })
  it('missing cart param', function (done) {
    request('http://localhost:7865/cart/', function(error, response, body) {
      chai.expect(response.statusCode).to.equal(404);
      done();
    })
  })

});
