# class Contact:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number

class ContactList:
    def __init__(self, name, contacts):
        self.name = name
        self.contacts = contacts

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.contacts.sort(key=lambda x: x.name)
        return self.contacts

    def remove_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts.pop(i)
                return self.contacts
        return None

    def find_shared_contacts(self, contactlst):
        shared = []
        for contact in self.contacts:
            if contact in contactlst.contacts:
                shared.append(contact)
        return shared

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

print(my_friends_list.find_shared_contacts(my_work_buddies))
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]

