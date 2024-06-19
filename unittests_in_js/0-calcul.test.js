//test cases of calculateNumber function
// const calculateNumber = require('./0-calcul.js');
// const assert = require('assert');

// describe('Test calculateNumber function', () => {
//     it('test the sum with rounded up numbers', () => {
//         assert.strictEqual(calculateNumber(0, 0), 0);
//         assert.strictEqual(calculateNumber(1.8, 0), 2);
//         assert.strictEqual(calculateNumber(2, 3), 5);
//         assert.strictEqual(calculateNumber(5, 2.8), 8);
//         assert.strictEqual(calculateNumber(1.2, 3), 4);
//         assert.strictEqual(calculateNumber(1.5, 3.7), 5);
//     });
//     it('test the sum with negative numbers', () => {
//         assert.strictEqual(calculateNumber(20, -3), 17);
//         assert.strictEqual(calculateNumber(0, -3), -3);
//         assert.strictEqual(calculateNumber(-5, 1), 4);
//         assert.strictEqual(calculateNumber(-20, -3), -23);
//         assert.strictEqual(calculateNumber(-20, 20), 0);
//     });
//     it('test if miss argument(s)', () => {
//         assert.strictEqual(isNaN(calculateNumber(3)), true);
//         assert.strictEqual(isNaN(calculateNumber()), true);
//     });
// });
const calculateNumber = require('./0-calcul')
const assert = require('assert');


describe ("Test suite", function() {
	it("Tests that a and b are rounded properly using Math.round()", function() {
		assert.equal(calculateNumber(1.1, 2.2), 3);
		assert.equal(calculateNumber(1.4, 1,4), 2);
		assert.equal(calculateNumber(1.5, 1.5), 4);
		assert.equal(calculateNumber(1.6, 1.6), 4);
		assert.equal(calculateNumber(1.7, 1), 3);
		assert.equal(calculateNumber(1, 1.8), 3);
		assert.equal(calculateNumber(-5, 0.5), -4);
		assert.equal(calculateNumber(0, -10.98), -11);
		assert.equal(calculateNumber(1.1, 1.9), 3);
		assert.equal(calculateNumber(1.1, 0), 1);
	});
})