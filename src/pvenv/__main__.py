from dataclasses import asdict

from pvenv import subcommands
from pvenv.lib.cli import parse_args


def main() -> None:
    args = parse_args()
    if args.in_subcommand is not None:
        subcommands.invenv.Command(
            base_dirs=args.base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            **asdict(args.in_subcommand),
        ).run()
    elif args.init_subcommand is not None:
        subcommands.initvenv.Command(
            base_dirs=args.base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            **asdict(args.init_subcommand),
        ).run()
    elif args.out_subcommand is not None:
        subcommands.outvenv.Command(
            base_dirs=args.base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            **asdict(args.out_subcommand),
        ).run()
    elif args.activate_subcommand is not None:
        subcommands.avenv.Command(
            base_dirs=args.base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            **asdict(args.activate_subcommand),
        ).run()
    elif args.deactivate_subcommand is not None:
        subcommands.dvenv.Command(
            base_dirs=args.base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            **asdict(args.deactivate_subcommand),
        ).run()
    elif args.list_subcommand is not None:
        subcommands.lsvenv.Command(
            base_dirs=args.base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            **asdict(args.list_subcommand),
        ).run()
    elif args.make_subcommand is not None:
        subcommands.mkvenv.Command(
            base_dirs=args.base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            **asdict(args.make_subcommand),
        ).run()
    elif args.rm_subcommand is not None:  # pragma: no branch
        subcommands.rmvenv.Command(
            base_dirs=args.base_dirs,
            dry_run=args.dry_run,
            verbosity=args.verbosity,
            **asdict(args.rm_subcommand),
        ).run()
