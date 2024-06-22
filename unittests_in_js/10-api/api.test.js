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
    });
  });

  it('invalid int id', function (done) {
    request('http://localhost:7865/cart/hello', function(error, response, body) {
      chai.expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('GET /available_payments returns expected info', function (done) {
    request('http://localhost:7865/available_payments', function (error, response, body) {
      // Assert status code and response type
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(response.headers['content-type']).to.include('application/json');
  
      // Parse the JSON response body
      const data = JSON.parse(body);
  
      // Assert expected properties and values in the response object
      chai.expect(data).to.have.property('payment_methods');
      chai.expect(data.payment_methods).to.be.an('object');
      chai.expect(data.payment_methods).to.deep.equal({
        credit_cards: true,
        paypal: false,
      });
  
      done();
    });
  });

  it('missing cart param', function (done) {
    request('http://localhost:7865/cart/', function(error, response, body) {
      chai.expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('POST /login returns welcome message', function (done) {
    const loginData = {
      userName: 'test_user', // Replace with a test username
    };
  
    // Configure request options for POST with JSON data
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: loginData, // Send data as JSON in the request body
    };
  
    request(options, function (error, response, body) {
      // Assert status code and response type (optional)
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(response.headers['content-type']).to.include('text/plain'); // May vary depending on your API
  
      // Assert expected response message
      chai.expect(body).to.equal(`Welcome ${loginData.userName}`);
  
      done();
    });
  });

});
