function venv {
    case "$1" in
    in)
        invenv "${@:2}"
        ;;
    out)
        outvenv "${@:2}"
        ;;
    list)
        lsvenv "${@:2}"
        ;;
    rm)
        rmvenv "${@:2}"
        ;;
    *)
        pvenv "$@"
        return
        ;;
    esac
}

function invenv {
    local IFS=$'\n'
    for command in $(pvenv in "$@"); do
        eval "${command}"
    done
}

function outvenv {
    local IFS=$'\n'
    for command in $(pvenv out); do
        eval "${command}"
    done
}

function lsvenv {
    pvenv list "$@"
}

function rmvenv {
    pvenv rm "$@"
}
