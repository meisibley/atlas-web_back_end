//test cases of calculateNumber function
const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('Test calculateNumber function', () => {
    it('test the sum with rounded up numbers', () => {
        assert.strictEqual(calculateNumber(0, 0), 0);
        assert.strictEqual(calculateNumber(1.8, 0), 2);
        assert.strictEqual(calculateNumber(2, 3), 5);
        assert.strictEqual(calculateNumber(5, 2.6), 8);
        assert.strictEqual(calculateNumber(1.2, 3), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
    it('test the sum with negative numbers', () => {
        assert.strictEqual(calculateNumber(20, -3), 17);
        assert.strictEqual(calculateNumber(0, -3), -3);
        assert.strictEqual(calculateNumber(-5, 1), 4);
        assert.strictEqual(calculateNumber(-20, -3), -23);
        assert.strictEqual(calculateNumber(-20, 20), 0);
    });
    it('test if miss argument(s)', () => {
        assert.strictEqual(isNaN(calculateNumber(3)), true);
        assert.strictEqual(isNaN(calculateNumber()), true);
    });
});
