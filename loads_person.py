import json

url_type = ['person_url', 'list_of_persons_url']


class Person:
    def get(json_file):
        return open(json_file)

    def format_json(input_json, url):
        if url == 'person_url':
            persons = json.load(input_json)
            for person in persons:
                print(person)
        elif url == 'list_of_persons_url':
            persons = json.load(input_json)
            for person in persons:
                print(f'{{"full_name": "{person["full_name"]}","profile_url": "{person["profile_url"]}"}}')


if __name__ == "__main__":
    f = Person.get('person.json')
    Person.format_json(f, url_type[0])
