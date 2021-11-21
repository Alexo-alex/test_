import json

url_type = ['company_url', 'list_of_company_url']


class Person:
    def get(json_file):
        return open(json_file)

    def format_json(input_json, url):
        if url == 'company_url':
            persons = json.load(input_json)
            for person in persons:
                print(person)
        elif url == 'list_of_company_url':
            persons = json.load(input_json)
            for person in persons:
                print(f'{{"name": "{person["name"]}","company_url": "{person["company_url"]}"}}')


if __name__ == "__main__":
    f = Person.get('company.json')
    Person.format_json(f, url_type[1])
