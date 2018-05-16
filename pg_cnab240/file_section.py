import json
from pg_cnab240.attribute import Attribute


class FileSection:
    default_date_format = "%d%m%Y"
    default_datetime_format = "%d%m%Y %H%M%S"
    default_time_format = "%H%M%S"

    def __init__(self, section_name, data, attributes):
        self.bank = None
        self.section_name = section_name
        self.attributes = attributes
        
        self.data = data
        if self.data is None:
            self.data = dict()

        self.transform_attributes()
        if self.data is not None:
            self.associate_data()
    
    def transform_attributes(self):
        for attr, data in self.attributes.items():
            self.attributes[attr] = Attribute(attr, data['type'], data['length'], data['start'], data['end'], data['default'], data['pad_content'], data['pad_direction'], data['required'], self.default_datetime_format, self.default_date_format, self.default_time_format)
    
    def associate_data(self):
        if self.data:
            if self.bank:
                self.data['bank_code'] = self.bank.code
             
            for name, attr in self.attributes.items():
                if name in self.data:
                    self.attributes[name].set_value(self.data[name])
                elif attr.is_required():
                    raise Exception('The ' + self.section_name + ' Attribute "' + name + '" is required')
    
    def get_dict(self):
        response = dict()
        for attr_name, attr in self.attributes.items():
            response[attr_name] = attr.get_value()
        return response
    
    def get_json(self):
        return json.dumps(self.get_dict())
    
    def to_line(self):
        line = ''
        for attr_name, attr in self.attributes.items():
            line += attr.get_value()
        return line
    
    def get_required_attributes(self):
        required_attributes = []
        for attr_name, attr in self.attributes.items():
            if attr.is_required():
                required_attributes.append(attr)
        return required_attributes
    
    def set_bank(self, bank):
        self.bank = bank
    
    def set_data(self, data=dict()):
        for attribute, value in data.items():
            self.data[attribute] = value
        self.associate_data()
