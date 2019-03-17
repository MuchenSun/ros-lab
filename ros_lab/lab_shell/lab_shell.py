import cmd, sys
import docker
import webbrowser

class lab_shell(cmd.Cmd):
    intro = '\nThe ROS Virtual Lab. Type \'help\' or \'?\' for help.'
    prompt = '\nLab >> '
    lab_state = {
        0: 'not loaded',
        1: 'loaded',
    }
    lab_list = {}
    client = docker.from_env()
    container_id = []
    image_id = []

    def __init__(self):
        super(lab_shell, self).__init__()
        self.lab_list = {
            0: ['TurtleBot3 Basic Lab', self.lab_state[0], 'muchensun/ros_turtlebot3_vnc:v0.2']
        }

    def do_list_lab(self, arg):
        'list all the labs'
        print('%-15s' % 'Lab Number', end='')
        print('%-30s' % 'Lab Name', end='')
        print('%-20s' % 'Lab State')
        for index in range(0, len(self.lab_list)):
            print('%-15s' % str(index), end='')
            print('%-30s' % self.lab_list[index][0], end='')
            print('%-20s' % self.lab_list[index][1])

    def do_load_lab(self, arg):
        'input lab number to load lab'
        try:
            arg = int(arg)
        except ValueError:
            print("Argumene is required. Typr \"help start_lab\" for more information")
        else:
            if arg in self.lab_list:
                print("The docker image " + "\"" + self.lab_list[arg][2] + "\"" + " is loading, please wait ...")
                temp_image = self.client.images.pull(self.lab_list[arg][2])
                self.lab_list[arg][1] = self.lab_state[1]
                self.image_id.append(temp_image.id)
                print("The docker image " + "\"" + self.lab_list[arg][2] + "\"" + " is loaded.")
                
            else:
                print('Invalid lab number!')

    def do_start_lab(self, arg):
        'input lab number to start lab'
        try:
            arg = int(arg)
        except ValueError:
            print("Argumene is required. Typr \"help start_lab\" for more information.")
        else:
            self.do_load_lab(arg)
            if arg in self.lab_list:
                temp_container = self.client.containers.run(self.lab_list[arg][2],
                                                            command='echo TurtleBot3 Basic Lab Initialized',
                                                            ports={'80/tcp': ('127.0.0.1', 6080)}, detach=True)
                self.container_id.append(temp_container.id)
                print("Lab successfully initialized. Visit 127.0.0.1:6080 in your browser.")
                webbrowser.open_new("127.0.0.1:6080")
            else:
                print('Invalid lab number!')

    def do_stop_and_save_lab(self, arg):
        'stop lap and save state'
        pass

    def do_quit(self, arg):
        'quit the lab'
        print('quit the lab')
        return True

