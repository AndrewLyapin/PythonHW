import view
import model
import text


def search_modul():
    word = view.input_data(text.input_search_word)
    result = model.search(word)
    view.show_contact(result, text.empty_search(word))

def start():
    while True:
        user_select = view.show_menu()
        match user_select:
            case 1:
                model.open_file()
                view.print_msg(text.load_sucessful)
            case 2:
                model.save_file()
                view.print_msg(text.save_sucessful)
            case 3:
                pb = model.phone_book
                view.show_contact(pb, text.empty_book)
            case 4:
                contact = view.input_new_contact(text.fields_new_contact)
                model.input_contact(contact)
                view.print_msg(text.new_contact_succesful(contact[0]))
            case 5:
                search_modul()
            case 6:
                search_modul()
                uid = view.input_number(text.input_rename_uid)
                rename = view.input_new_contact(text.fields_rename_contact)
                name = model.change_contact(uid, rename)
                view.print_msg(text.rename_sucessful(name))
            case 7:
                search_modul()
                uid = view.input_number(text.input_del_uid)
                name = model.delete_contact(uid)
                view.print_msg(text.contact_deleted(name))
            case 8:
                view.print_msg(text.good_bye)
                break