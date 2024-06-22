const chai = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
    it('SUM, it round the first argument', () => {
        chai.expect(calculateNumber('SUM', 1.0, 0)).to.equal(1);
        chai.expect(calculateNumber('SUM', 1.3, 0)).to.equal(1);
        chai.expect(calculateNumber('SUM', 1.7, 0)).to.equal(2);
    });

    it('SUM, it round the second argument', () => {
        chai.expect(calculateNumber('SUM', 0, 1.0)).to.equal(1);
        chai.expect(calculateNumber('SUM', 0, 1.3)).to.equal(1);
        chai.expect(calculateNumber('SUM', 0, 1.7)).to.equal(2);
    });

    it('SUM, it should return the right number', () => {
        chai.expect(calculateNumber('SUM', 1.3, 0)).to.equal(1);
        chai.expect(calculateNumber('SUM', 0, 1.2)).to.equal(1);
        chai.expect(calculateNumber('SUM', 1.3, 1.3)).to.equal(2);
        chai.expect(calculateNumber('SUM', 1.7, 1.2)).to.equal(3);
        chai.expect(calculateNumber('SUM', 1.3, 1.8)).to.equal(3);
        chai.expect(calculateNumber('SUM', 1.6, 1.8)).to.equal(4);
    });

    it('SUBTRACT, it round the first argument', () => {
        chai.expect(calculateNumber('SUBTRACT', 1.0, 0)).to.equal(1);
        chai.expect(calculateNumber('SUBTRACT', 2.3, 1)).to.equal(1);
        chai.expect(calculateNumber('SUBTRACT', 2.7, 1)).to.equal(2);
    });

    it('SUBTRACT, it round the second argument', () => {
        chai.expect(calculateNumber('SUBTRACT', 0, 1.0)).to.equal(-1);
        chai.expect(calculateNumber('SUBTRACT', 2, 1.3)).to.equal(1);
        chai.expect(calculateNumber('SUBTRACT', 2, 1.7)).to.equal(0);
    });

    it('SUBTRACT, it should return the right number', () => {
        chai.expect(calculateNumber('SUBTRACT', 2.3, 1.4)).to.equal(1);
        chai.expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        chai.expect(calculateNumber('SUBTRACT', 1.5, 4.3)).to.equal(-2);
        chai.expect(calculateNumber('SUBTRACT', 4.7, 1.5)).to.equal(3);
        chai.expect(calculateNumber('SUBTRACT', 0, 4.7)).to.equal(-5);
        chai.expect(calculateNumber('SUBTRACT', 1.2, 0)).to.equal(1);
    });

    it('DIVIDE, it round the first argument', () => {
        chai.expect(calculateNumber('DIVIDE', 2.3, 2)).to.equal(1);
        chai.expect(calculateNumber('DIVIDE', 3.7, 2)).to.equal(2);
        chai.expect(calculateNumber('DIVIDE', 3.7, 0)).to.equal('Error');
    });

    it('DIVIDE, it round the second argument', () => {
        chai.expect(calculateNumber('DIVIDE', 4, 2.3)).to.equal(2);
        chai.expect(calculateNumber('DIVIDE', 4, 1.5)).to.equal(2);
        chai.expect(calculateNumber('DIVIDE', 2, 0.2)).to.equal('Error');
    });

    it('DIVIDE, it should return the right number', () => {
        chai.expect(calculateNumber('DIVIDE', 5.8, 2.3)).to.equal(3);
        chai.expect(calculateNumber('DIVIDE', 4.4, 1.5)).to.equal(2);
        chai.expect(calculateNumber('DIVIDE', 2.2, 1.2)).to.equal(2);
        chai.expect(calculateNumber('DIVIDE', 9.9, 1.6)).to.equal(5);
        chai.expect(calculateNumber('DIVIDE', 0.4, 3.5)).to.equal(0);
        chai.expect(calculateNumber('DIVIDE', 2.2, 0.7)).to.equal(2);
    });
});
