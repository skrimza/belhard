class ConfiqParser:
    text = '''
    [section1]
    key1=value1
    key2=value2

    [section2]
    key3=value3
    key4=value4
    key5=value5
    '''
    sections = {}

    def parse(self):
        new_text = self.text.split('\n')
        clean_text = [i.strip() for i in new_text]
        for i in clean_text:
            if i.startswith('['):
                cur_section = i[1:-1]
                self.sections[cur_section] = {}
            elif '=' in i:
                key, value = i.split('=')
                self.sections[cur_section][key.strip()] = value.strip()

    def __dict__(self):
        return self.sections
    
    def get(self, name: str, key: str):
        for section, section_key in self.sections.items():
            for key_num, value_num in section_key.items():
                if name == section and key == key_num:
                    return value_num
        raise ValueError('ValueError Ильюха')
    
    def add_section(self, new_section):
        if new_section not in self.sections.keys():
            self.sections[new_section] = {}
            return new_section
        else:
            raise ValueError('ValueError, братан')

    def add_param(self, name, new_key, new_value):
        if name in self.sections:
            section = self.sections[name]
            if new_key in section:
                section[new_key] = new_value
            else:
                section.update({new_key: new_value})
        else:
            raise ValueError('нет такой секции')
        return self.sections


    def has_section(self, name):
        return name in self.sections

    def has_param(self, name, param):
        if name in self.sections:
            section = self.sections[name]
            return param in section.keys()
        else:
            raise ValueError('нет такой секции')

    def del_section(self, name):
        if name in self.sections:
            del self.sections[name]
        return self.sections
        

    def del_param(self, name, name_param):
        if name in self.sections:
            section = self.sections[name]
            if name_param in section:
                del self.sections[name_param]

    def __repr__(self) -> str:
        list_sections = []
        for section, dict_keys in self.sections.items():
            list_sections.append(f'[{section}]')
            for key, value in dict_keys.items():
                list_sections.append(f'{key}={value}')
        return '\n'.join(list_sections)
   
res = ConfiqParser()
res.parse()
print(res.sections)
value = res.get('section1', 'key1')
print(value)
new_section = res.add_section('section3')
print(new_section)
add_param = res.add_param('section3', 'key10', 'value10')
print(add_param)
has_section = res.has_section('section3')
print(has_section)
has_param = res.has_param('section3', 'key15')
print(has_param)
del_section = res.del_section('section3')
print(del_section)
print(res.__repr__())