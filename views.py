from built_to_serve_arazi47.views import route, BaseView, render
from built_to_serve_arazi47.custom_content_parser import transform_template_to_code
from datetime import datetime
from repository import GuestBookRepository
from models import GuestBook

@route("/")
@route("/index.html")
class Index(BaseView):
    def __init__(self, file_path, status_code=200, content_type="text/html") -> None:
        super().__init__(file_path, status_code, content_type)

    def build_GET_response(self) -> str:
        with open(self.file_path) as f:
            return f.read()

@route("/guesthome.html")
class GuestHome(BaseView):
    def __init__(self, file_path="", status_code=200, content_type="text/html") -> None:
        super().__init__(file_path, status_code, content_type)

    def build_GET_response(self) -> str:
        return transform_template_to_code(self.file_path, {"gbrepo": GuestBookRepository()})

    def build_POST_response(self, fields) -> str:
        username = fields["username"][0]
        comment = fields["comment"][0]

        gbrepo = GuestBookRepository()
        gbentry = GuestBook()
        gbentry.username = username
        gbentry.comment = comment
        gbentry.posted_on = datetime.now().strftime("%B %d, %Y %I:%M%p")
        gbrepo.save(gbentry)

        return render("/")


@route("/adminhome.html")
class AdminHome(BaseView):
    def __init__(self, file_path="", status_code=200, content_type="text/html") -> None:
        super().__init__(file_path, status_code, content_type)

    def build_GET_response(self) -> str:
        return transform_template_to_code(self.file_path, {"gbrepo": GuestBookRepository(), "authors": ["asd", 1]})
    
    def build_POST_response(self, fields) -> str:
        id = int(fields["id"][0])
        gbrepo = GuestBookRepository()
        if "submit_update_entry" in fields:
            username = fields["username"][0]
            comment = fields["comment"][0]
            gbrepo.save(GuestBook(id, username, comment, datetime.now().strftime("%B %d, %Y %I:%M%p")))
        elif "submit_delete_entry" in fields:
            gbrepo.delete(id)
        else:
            print("Unknown POST request.")

        return render("/adminhome.html")
