"""
Prints a message to stdout given by either a flag or an environment variable.
For flag, pass --message=<a message> when running.
For environment variable, set MESSAGE=<a message> and then execute the program.
"""
from os import environ

from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string('message', 'Hello, World!', 'Message to print to the console.')


def main(argv):
    print("Running app...")

    if message := environ.get('MESSAGE'):
        print(f'Message from env var is: {message}')
    else:
        print(f'Message from flags is: {FLAGS.message}')


if __name__ == '__main__':
    app.run(main)
