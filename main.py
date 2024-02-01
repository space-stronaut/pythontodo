def main():
    mylist = []
    while(True):
        print("----- TODO -----")
        print("1. Get List")
        print("2. Create Todo")
        print("3. Remove Todo")
        print("4. Exit")
        inputs = input("Masukkan input : ")
        if inputs == "1":
            for x in mylist:
                print(x)
        elif inputs == "2":
            todoInput = input("Masukkan Todo : ")
            mylist.append(todoInput)
            for x in mylist:
                print(x)
            print("Todo " + todoInput + " berhasil dibuat")
        elif inputs == "3":
            if len(mylist) < 1:
                print("Tidak ada todo list, harap buat dulu")
            else :
                for x in mylist:
                    print(x)
                todoInput = input("Masukkan Todo yang ingin dihapus : ")
                mylist.remove(todoInput)
                for x in mylist:
                    print(x)
                print("Todo " + todoInput + " berhasil dihapus")
        else :
            print("Terima kasih :)")
            return False

main()
