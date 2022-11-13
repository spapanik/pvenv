function venv {
    case "$1" in
    list)
        lsvenv "${@:2}"
        ;;
    *)
        pvenv "$@"
        return
        ;;
    esac
}

function lsvenv {
    pvenv list "$@"
}
