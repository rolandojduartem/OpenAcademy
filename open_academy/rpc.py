import xmlrpc.client


class RPC():
    def __init__(self):
        self.url = 'http://localhost:8069'
        self.database = 'demo_rolo'
        self.username = 'admin'
        self.password = 'admin'

        self.common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % self.url)
        self.uid = self.common.authenticate(self.database, self.username, self.password, {})
        self.models = xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % self.url)

    def _view(self, model):
        session_ids = self.models.execute_kw(
            self.database,
            self.uid,
            self.password,
            model,
            'search',
            [[]]
        )
        if model == 'session':
            fields = ['name', 'number_seat']
        elif model == 'course':
            fields = ['title']
        sessions = self.models.execute_kw(
            self.database,
            self.uid,
            self.password,
            model,
            'read',
            [session_ids],
            {'fields': fields}
        )
        for session in sessions:
            print(session)

    def _create(self):
        print("the course ids are:")
        self._view("course")
        main_fields = ["name", "course_id", "number_seat"]
        input_new_data = input(
            'Introduce data for the %s, %s, %s fields (Separated with comma): ' % tuple(main_fields)
        )
        args = input_new_data.split(",")
        create_data = {}
        create_data['name'] = args[0].strip()
        create_data['course_id'] = int(args[1].strip())
        create_data['number_seat'] = int(args[2].strip())
        self.models.execute_kw(
            self.database,
            self.uid,
            self.password,
            'session',
            'create',
            [create_data],
        )
        success_message = "Session %s was created!" % create_data['name']
        print(success_message)

    def run(self):
        while True:
            choose = input('Do you want to view / create / exit? (v/c/e); ')
            if choose in ['v', 'view']:
                self._view('session')
            if choose in ['c', 'create']:
                self._create()
            elif choose in ['e', 'exit']:
                break


if __name__ == '__main__':
    rpc = RPC()
    rpc.run()
