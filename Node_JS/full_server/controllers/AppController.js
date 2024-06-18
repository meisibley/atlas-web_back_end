//return a 200 status and the hello message
class AppController {
  static getHomepage(request, response) {
    response.send(200, 'Hello Holberton School!');
  }
}

module.exports = AppController;
