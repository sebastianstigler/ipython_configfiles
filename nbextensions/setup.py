import os
from IPython.html.nbextensions import install_nbextension
from IPython.html.services.config import ConfigManager
from IPython.utils.path import locate_profile


base_dir = os.path.abspath(os.path.dirname(__file__))


def install(extension, use_symlink=False, profile='default', enable=True):
    # Install the livereveal code.
    ext_dir = os.path.join(base_dir, extension)
    install_nbextension(ext_dir, symlink=use_symlink,
                        overwrite=use_symlink, user=True)

    if enable:
        # Enable the extension in the given profile.
        profile_dir = locate_profile(profile)
        cm = ConfigManager(profile_dir=profile_dir)
        cm.update('notebook', {"load_extensions": {extension + "/main": True}})


def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands',
                                       help='additional help')

    install_parser = subparsers.add_parser('install')
    install_parser.add_argument('--develop', action='store_true',
                                help=("Install extensions  as a "
                                      "symlink to the source."))
    install_parser.add_argument('--no-enable', action='store_true',
                                help="Install but don't enable the extension.")
    install_parser.add_argument('--profile', action='store', default='default',
                                help=("The name of the profile to use."))

    args = parser.parse_args(sys.argv[1:])
    for a, dirs, b in os.walk(base_dir):
        for ext in dirs:
            install(ext, use_symlink=args.develop, profile=args.profile,
            enable=(not args.no_enable))
        break

if __name__ == '__main__':
    main()
