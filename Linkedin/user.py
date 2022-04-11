import json
from .graph import Graph


class User:
    __users = {}
    __graph = Graph()

    def __init__(self, id: int, name: str, birth: str, university: str, field: str, workplace: str, specialties: list,
                 connected_id: set):

        self.__id = id
        self.__name = name
        self.__birth = birth
        self.__university = university
        self.__field = field
        self.__workplace = workplace
        self.__specialties = specialties  # list of specialties(list of strings)
        self.__connected_id = set(map(int, connected_id))  # list of id(list of integers)

        User.add_to_graph(self)

        self.__users[id] = self

    @classmethod
    def get_graph(cls):
        return cls.__graph

    @property
    def id(self):
        return self.__id

    @property
    def university(self):
        return self.__university

    @property
    def workplace(self):
        return self.__workplace

    @property
    def field(self):
        return self.__field

    @property
    def specialties(self):
        return self.__specialties

    @property
    def connected_id(self):
        return self.__connected_id

    @classmethod
    def read_from_json(cls, path: str):
        for obj in json.load(open(path, 'r')):
            User(int(obj['id']), obj['name'], obj['dateOfBirth'], obj['universityLocation'],
                 obj['field'], obj['workplace'], obj['specialties'], obj['connectionId'])

    @classmethod
    def get_user(cls, key: int):
        return cls.__users.get(key)

    @classmethod
    def new_id(cls):
        return len(cls.__users)

    @classmethod
    def remove_user(cls, key: int):

        if key not in cls.__users.keys():
            return

        for user in cls.__users.values():
            if key in user.connected_id:
                user.connected_id.remove(key)

        cls.__graph.remove_node(key)
        cls.__users.pop(key)

    def add_connection(self, user_id: int):

        if user_id not in User.__users.keys():
            raise Exception("There is No User with this ID")
        self.connected_id.add(user_id)
        self.get_graph().add_edge(self.id, user_id, 1)

    def remove_connection(self, user_id: int):

        if user_id not in self.connected_id:
            raise Exception("There is No User with this ID")

        self.connected_id.remove(user_id)
        User.get_user(user_id).connected_id.remove(self.id)

        User.get_graph().remove_edge(self.id, user_id)


    @classmethod
    def get_score(cls, first_id: int, second_id: int, distance: int):

        score = 0

        first_user: User = cls.get_user(first_id)
        second_user: User = cls.get_user(second_id)

        if first_user is None or second_user is None:
            raise Exception("there is no user with this ID")

        if first_user.__field == second_user.__field:
            score += 5

        if first_user.university == second_user.university:
            score += 2

        if first_user.workplace == second_user.workplace:
            score += 4

        s3 = set.intersection(set(first_user.specialties), set(second_user.specialties))
        score += len(s3) * 3

        score -= distance

        return score

    @classmethod
    def add_to_graph(cls, user):
        user: User

        cls.__graph.add_node(user.id)
        for adjacent in user.connected_id:
            cls.__graph.add_node(adjacent)
            cls.__graph.add_edge(user.id, adjacent, 1)

    def get_all_adjacent(self):
        ls = []
        for adjacent in self.connected_id:
            ls.extend(User.__graph.depth_first_traverse(adjacent))
        return ls

    def following_offer(self):
        return self.filter_offers(self.get_all_adjacent())

    def filter_offers(self, offers: list):
        ls = [path for path in offers if self.id not in path]
        ls = User.remove_if_adjacent(self.id, ls)
        User.shortest_connection(ls)
        ls = User.remove_repetitive_connections(ls)
        ls = User.filter_by_score(self.id, ls)
        final_list = self.remove_repetitive_target(ls)
        return final_list

    @classmethod
    def remove_if_adjacent(cls, user_id, offers: list):
        user = cls.get_user(user_id)
        return [path for path in offers if path[-1] not in user.connected_id]

    @classmethod
    def shortest_connection(cls, offers: list):

        for i in range(0, len(offers)):
            target = offers[i][-1]

            for j in range(0, len(offers)):
                second_target = offers[j][-1]

                if target != second_target:
                    continue

                first_condition = target == second_target
                second_condition = len(offers[j]) > len(offers[i])

                if first_condition and second_condition:
                    offers[j] = offers[i]

    @classmethod
    def remove_repetitive_connections(cls, connections: list):
        final_list = []
        for element in connections:
            if element not in final_list:
                final_list.append(element)

        return final_list

    @classmethod
    def filter_by_score(cls, user_id: int, offers: list):
        check_score = lambda offer: cls.get_score(user_id, offer[-1], len(offer)) > 4
        offers = list(filter(check_score, offers))
        return offers

    @classmethod
    def remove_repetitive_target(cls, offers: list):
        targets = set(target[-1] for target in offers)
        final_offers = []
        for path in offers:

            target = path[-1]
            if target in targets:
                final_offers.append(path)
                targets.remove(target)

        return final_offers

    def __str__(self):
        s1 = f"{self.__id} - {self.__name} - Birth:{self.__birth} - University:{self.university} - Work place:{self.workplace}"
        s2 = f"- Field:{self.field} - specialties:{self.specialties} - connections:{self.connected_id}"
        return s1 + s2

    def show_connections(self):
        info = lambda user: print(user.__name, "university:" + user.university, "Field:" + user.field,
                                  "workplace:" + user.workplace, "specialties:" + str(user.specialties),
                                  sep=" - ", end="\n\n")
        [info(User.get_user(adjacent)) for adjacent in self.connected_id]

    def show_offers(self):

        all_offers = self.following_offer()
        for path in all_offers:
            target: User = User.get_user(path[-1])
            print(target.id, target.__name, end=" --- ")

            for user_id in path:
                print(User.get_user(user_id).__name, end=" -> ")
            print()
