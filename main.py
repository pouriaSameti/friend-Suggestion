from Linkedin.user import User
import os


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':

    User.read_from_json("users2.json")

    while True:

        print("<1>Login")
        print("<2>Create User")
        print("<3>Exit")

        command = int(input("Select a Command\t"))

        if command == 1:
            clean()
            try:
                user_id = int(input("Enter ID\t"))
                user: User = User.get_user(user_id)

                if user is None:
                    raise Exception("There is No User with this ID")

            except Exception as exp:
                print(exp)

            else:
                while True:

                    print("<1>All Connections")
                    print("<2>Offers")
                    print("<3>Add Connection")
                    print("<4>Remove Connection")
                    print("<5>Delete Account")
                    print("<6>Back")

                    new_command = int(input("Select a Command\t"))

                    if new_command == 1:
                        clean()
                        user.show_connections()

                    elif new_command == 2:
                        clean()
                        user.show_offers()

                    elif new_command == 3:
                        clean()
                        new_id = int(input("Enter user ID\t"))
                        try:
                            user.add_connection(new_id)
                        except Exception as exp:
                            print(exp)

                    elif new_command == 4:
                        clean()
                        new_id = int(input("Enter user ID\t"))
                        try:
                            user.remove_connection(new_id)
                        except Exception as exp:
                            print(exp)

                    elif new_command == 5:
                        clean()
                        User.remove_user(user.id)
                        print("Your Account Was Removed")
                        break

                    elif new_command == 6:
                        clean()
                        break

                    else:
                        try:
                            raise Exception("Invalid Input")

                        except Exception as e:
                            print(e)

        elif command == 2:
            clean()
            name = input("Enter Name\t")
            birth = input("Enter Your Birth\t")
            university = input("Enter Your University\t")
            field = input("Enter Your Field\t")
            workplace = input("Enter Your WorkPlace\t")
            specialities = input("Enter Your specialities\t").split(" ")

            u = User(User.new_id(), name, birth, university, field, workplace, specialities, set())
            print(u)
            print("User Was Added")

        elif command == 3:
            break

        else:
            try:
                raise Exception("Invalid Input")

            except Exception as e:
                print(e)

    # u1 = User(1, "arshia hemat", "1380/5/2", "UI", "CE", "morcot", ["Machine learning","Reinforcement learning","Blockchain programming"], ["2","3","4"])
    # u2 = User(2, "amirali goli", "1379/5/2", "UI", "CE", "mohaymen", ["Java programming","Django","Back-End"], ["1","4","5","6"])
    # u3 = User(3, "danial tavakoli", "1381/5/2", "UI", "CE", "-", ["Java programming","AI"], ["1","4","6"])
    # u4 = User(4, "mohamad eshagh", "1381/5/3", "UI", "CE", "msi", ["Kotlin programming","Android"], ["1","2","3"])
    # u5 = User(5, "ali ebrahimi", "1381/8/3", "UI", "CE", "-", ["Java programming","AI","Java FX"], ["2","6"])
    # u6 = User(6, "mehrshad farahani", "1381/8/13", "UI", "CE", "-", ["QT","C++ programming"], ["2","3","5","7"])
    # u7 = User(7, "naghi mamoli", "1340/8/3", "UB", "Ar", "Paytakht", ["Building","Welding","Plastering"], ["6"])

    # User.remove_user(2)
    # # print(u1.connected_id)
    # User.get_graph().get_graph()
    # print(u6.connected_id)

    # l1 = u1.get_all_adjacent()
    # print("get all adjacent", l1, end="\n\n")
    #
    # l2 = [path for path in l1 if u1.id not in path]
    # print(l2, end="\n\n")
    #
    # l3 = User.remove_if_adjacent(u1.id, l2)
    # print("remove_if_adjacent", l3, end="\n\n")
    #
    # User.shortest_connection(l3)
    # print("shortest_connection", l3, end="\n\n")
    #
    # l4 = User.remove_repetitive_connections(l3)
    # print("remove_repetitive_connections", l4, end="\n\n")
    #
    # l5 = User.filter_by_score(u1.id, l4)
    # print("filter_by_score", l5, end="\n\n")
    #
    # l6 = u1.remove_repetitive_target(l4)
    # print("remove_repetitive_target", l6, end="\n\n")


    # g = Graph()
    # g.add_node(1)
    # g.add_node(2)
    # g.add_node(3)
    # g.add_node(4)
    # g.add_node(5)
    # g.add_node(6)
    # g.add_node(7)
    # g.add_node(8)
    # g.add_node(9)
    # g.add_node(10)
    #
    # g.add_edge(1, 2, 25)
    # g.add_edge(2, 3, 25)
    # g.add_edge(2, 1, 25)
    # g.add_edge(3, 4, 25)
    # g.add_edge(3, 5, 25)
    # g.add_edge(4, 6, 25)
    # g.add_edge(4, 1, 25)
    # g.add_edge(5, 7, 25)
    # g.add_edge(7, 10, 25)
    #
    # g.add_edge(1, 8, 25)
    # g.add_edge(8, 9, 25)

    # print(g.adjacency_list.get(g.nodes.get(1)))
    #
    # x = g.depth_first_traverse(1)
    # for a in x:
    #     print(a)
    # g.get_graph()
    # print("\n\n")

    # g.remove_edge(1, 4)

    # g.remove_node(1)
    #
    # g.get_graph()
    # print("\n\n")
