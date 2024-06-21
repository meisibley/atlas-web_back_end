const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
    it('SUM, it round the first argument', () => {
        assert.equal(calculateNumber('SUM', 1.0, 0), 1);
        assert.equal(calculateNumber('SUM', 1.3, 0), 1);
        assert.equal(calculateNumber('SUM', 1.7, 0), 2);
    });

    it('SUM, it round the second argument', () => {
        assert.equal(calculateNumber('SUM', 0, 1.0), 1);
        assert.equal(calculateNumber('SUM', 0, 1.3), 1);
        assert.equal(calculateNumber('SUM', 0, 1.7), 2);
    });

    it('SUM, it should return the right number', () => {
        assert.equal(calculateNumber('SUM', 1.3, 0), 1);
        assert.equal(calculateNumber('SUM', 0, 1.2), 1);
        assert.equal(calculateNumber('SUM', 1.3, 1.3), 2);
        assert.equal(calculateNumber('SUM', 1.7, 1.2), 3);
        assert.equal(calculateNumber('SUM', 1.3, 1.8), 3);
        assert.equal(calculateNumber('SUM', 1.6, 1.8), 4);
    });

    it('SUBTRACT, it round the first argument', () => {
        assert.equal(calculateNumber('SUBTRACT', 1.0, 0), 1);
        assert.equal(calculateNumber('SUBTRACT', 2.3, 1), 1);
        assert.equal(calculateNumber('SUBTRACT', 2.7, 1), 2);
    });

    it('SUBTRACT, it round the second argument', () => {
        assert.equal(calculateNumber('SUBTRACT', 0, 1.0), -1);
        assert.equal(calculateNumber('SUBTRACT', 2, 1.3), 1);
        assert.equal(calculateNumber('SUBTRACT', 2, 1.7), 0);
    });

    it('SUBTRACT, it should return the right number', () => {
        assert.equal(calculateNumber('SUBTRACT', 2.3, 1.4), 1);
        assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        assert.equal(calculateNumber('SUBTRACT', 1.5, 4.3), -2);
        assert.equal(calculateNumber('SUBTRACT', 4.7, 1.5), 3);
        assert.equal(calculateNumber('SUBTRACT', 0, 4.7), -5);
        assert.equal(calculateNumber('SUBTRACT', 1.2, 0), 1);
    });

    it('DIVIDE, it round the first argument', () => {
        assert.equal(calculateNumber('DIVIDE', 2.3, 2), 1);
        assert.equal(calculateNumber('DIVIDE', 3.7, 2), 2);
        assert.equal(calculateNumber('DIVIDE', 3.7, 0), 'Error');
    });

    it('DIVIDE, it round the second argument', () => {
        assert.equal(calculateNumber('DIVIDE', 4, 2.3), 2);
        assert.equal(calculateNumber('DIVIDE', 4, 1.5), 2);
        assert.equal(calculateNumber('DIVIDE', 2, 0.2), 'Error');
    });

    it('DIVIDE, it should return the right number', () => {
        assert.equal(calculateNumber('DIVIDE', 5.8, 2.3), 3);
        assert.equal(calculateNumber('DIVIDE', 4.4, 1.5), 2);
        assert.equal(calculateNumber('DIVIDE', 2.2, 1.2), 2);
        assert.equal(calculateNumber('DIVIDE', 9.9, 1.6), 5);
        assert.equal(calculateNumber('DIVIDE', 0.4, 3.5), 0);
        assert.equal(calculateNumber('DIVIDE', 2.2, 0.7), 2);
    });
});
