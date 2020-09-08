#!/usr/bin/env/python3
from shape_factory import ShapeFactory
from tax_file_factory import TaxFileFactory


def main():
    factory = ShapeFactory()
    square = factory.getShape('square')
    square.draw()
    circle = factory.getShape('circle')
    circle.draw()

    taxFileFactory = TaxFileFactory()
    quarterly = taxFileFactory.getTaxFile('quarterly')
    quarterly.buildEmployee()
    quarterly.buildPaycheck()
    annual = taxFileFactory.getTaxFile('annual')
    annual.buildEmployee()
    annual.buildPaycheck()


if __name__ == '__main__':
    main()
