#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Model(object):

    def __iter__(self):
        raise NotImplementedError

    def get(self, item):
        """
Devuelve un objeto con un método de llamada .items ()
        que itera sobre la clave, pares de valores de su información."""
        raise NotImplementedError

    @property
    def item_type(self):
        raise NotImplementedError


class ProductModel(Model):

    class Price(float):
        """
Una forma polimórfica de pasar un flotador con un particular
        __str__ funcionalidad."""

        def __str__(self):
            first_digits_str = str(round(self, 2))
            try:
                dot_location = first_digits_str.index('.')
            except ValueError:
                return (first_digits_str + '.00')
            else:
                return (first_digits_str +
                        '0' * (3 + dot_location - len(first_digits_str)))

    products = {
        'milk': {'price': Price(1.50), 'quantity': 10},
        'eggs': {'price': Price(0.20), 'quantity': 100},
        'cheese': {'price': Price(2.00), 'quantity': 10}
    }

    item_type = 'product'

    def __iter__(self):
        for item in self.products:
            yield item

    def get(self, product):
        try:
            return self.products[product]
        except KeyError as e:
            raise KeyError((str(e) + " not in the model's item list."))


class View(object):

    def show_item_list(self, item_type, item_list):
        raise NotImplementedError

    def show_item_information(self, item_type, item_name, item_info):
        """Buscará información de elementos al iterar sobre la clave, pares de valores generados por iteminfo.items ()"""
        raise NotImplementedError

    def item_not_found(self, item_type, item_name):
        raise NotImplementedError


class ConsoleView(View):

    def show_item_list(self, item_type, item_list):
        print(item_type.upper() + ' LIST:')
        for item in item_list:
            print(item)
        print('')

    @staticmethod
    def capitalizer(string):
        return string[0].upper() + string[1:].lower()

    def show_item_information(self, item_type, item_name, item_info):
        print(item_type.upper() + ' INFORMATION:')
        printout = 'Name: %s' % item_name
        for key, value in item_info.items():
            printout += (', ' + self.capitalizer(str(key)) + ': ' + str(value))
        printout += '\n'
        print(printout)

    def item_not_found(self, item_type, item_name):
        print('That %s "%s" does not exist in the records' %
              (item_type, item_name))


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self):
        items = list(self.model)
        item_type = self.model.item_type
        self.view.show_item_list(item_type, items)

    def show_item_information(self, item_name):
        try:
            item_info = self.model.get(item_name)
        except:
            item_type = self.model.item_type
            self.view.item_not_found(item_type, item_name)
        else:
            item_type = self.model.item_type
            self.view.show_item_information(item_type, item_name, item_info)


if __name__ == '__main__':

    model = ProductModel()
    view = ConsoleView()
    controller = Controller(model, view)
    controller.show_items()
    controller.show_item_information('cheese')
    controller.show_item_information('eggs')
    controller.show_item_information('milk')
    controller.show_item_information('arepas')
	
	
#Jorge Miguel Garcia Martinez

